import os
from slackclient import SlackClient
import time
import re
from Locations import Locations
from url_parser import url_parser as url
from cheapestprice import cheapest_price as cheapest
from sql import add_to_table as db

slack_client = SlackClient('KEY')

# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find
        bot commands. If a bot command is found, this function returns a tuple
        of command and channel. If its not found, then this function
        returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message
        text and returns the user ID which was mentioned. If there is no
        direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains
    # the remaining message
    return (matches.group(1),
            matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
        These are the available commands:
        peek <product> in <location> 
        peek <product> in <location> saveas <db>
        locations
        help
    """
    # Default response is help text for the user
    default_response = "Uknown command. Try *{}* for list of commands and usage.".format("help")

    # Finds and executes the given command, filling in response
    response = None
    
    # get the location, locations and locaiton ids
    l = Locations()
    provinces = l.get_provinces()
    province_ids = l.get_province_ids()    
    
    # locations
    if (command == "locations"):
        # print a message of the available locations
        provinces_string = "\n"
        for province_no in provinces:
            provinces_string += str(province_no) + ": " + provinces[province_no] + "\n"
        response = "Choose a locaton number from" + provinces_string

    # help
    elif (command == "help"):
        # print out all the usable commands
        response = "Here are list of commands to get you started." + (
        "\n\n*{}* _product name_ *{}* _location number_".format(
            "peek", "in"))  + (
        "\nEXAMPLE: To get the lowest gtx 1070 in Ontario") + (
        "\n peek gtx 1070 in 0") + (
        "\n\n*{}* _product name_ *{}* _location number_ *{}* _database name_".format(
            "peek", "in", "saveas")) + (
        "\n EXAMPLE: Find cheapest scarlett 2i2 in BC put it in 'mytable.db'") + (
        "\n peek scarlett 2i2 in 2 saveas mytable") + (
        "\n\n*{}*".format("locations")) + (
        "\n Lists all the location numbers")
    
    # peek <product name> in <location number>"
    # startswith peek
    # has " in "
    # product name = command[index(peek): index(in)]
    # location = command[index(in):]
    # remove beggining and end spaces from both 
    elif (command.startswith("peek ") and " in " in command):
        peek_right_index = command.find("peek ") + len("peek ")
        in_left_index = command.find(" in ")
        in_right_index = command.find(" in ") + len(" in ")
        
        # product is between peek and in
        product = command[peek_right_index:in_left_index]

        # check if a valid location filter is used
        after_in = command[in_right_index:]
        
        #print (after_in)
        # if a valid location filter is used
        if (after_in.strip().isdigit()):
            province_num = int(after_in.strip())
            website = url(product, province_num, provinces, province_ids)
            (product_name, product_price, link, date) = cheapest(website, product)
            
            response = "The cheapest " + product + " in " + provinces[province_num] + (
            " is the \n" + "<{}|{}>".format(link, product_name) + "\n") +  (
            "costing $" + str(product_price) + ", posted " + date)
           
        # check if the after_in is of the form <number> ... saveas <text>
        elif (" saveas " in after_in):
            
            saveas_left_index = after_in.find(" saveas ")
            saveas_right_index = after_in.find(" saveas ") + len(" saveas ")
            
            before_saveas = after_in[:saveas_left_index]
            # check if valid location is used
            if (after_in[:saveas_left_index].strip().isdigit()):
                
                # get the province num
                province_num = int(after_in[:saveas_left_index].strip())
                website = url(product, province_num, provinces, province_ids)
                (product_name, product_price, link, date) = cheapest(website, product)                
                
                table_name = after_in[saveas_right_index:]
                db(product_name, product_price,
                   provinces[province_num], link, date, table_name)
                response = "Added cheapest " + product + " in " + (
                    provinces[province_num]) + (
                " \n" + "<{}|{}>".format(link, product_name) + "\n") +  (
                "costing $" + str(product_price) + ", posted " + date + (
                "\nto the database named " + (
                    "*{}*".format(table_name) + "!")))

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )   

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        # get the command
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")