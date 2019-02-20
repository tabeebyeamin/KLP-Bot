import os
from slackclient import SlackClient
import time
import re
from Locations import Locations
from url_parser import url_parser as url
from cheapestprice import cheapest_price as cheapest
from sql import add_to_table as db

slack_client = SlackClient('xoxb-555934671814-554458209604-59vDExzQm3sHeNX9Xz9WfVjw')

# send message to #general channel
message = "hello"

#slack.chat.post_message('#general', message);

# message start to get it to start

# it will give you the option of whether you want to monitor or peek

#slack.chat.post_message("#general", text="hello", username="Kijiji Lowest Price Bot")

#slack.chat.me_message("#general", "yodog")
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "start"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command == EXAMPLE_COMMAND:
        response = "Sure, would you like to *{}* or *{}*?".format("peek", "monitor")

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )
def peek(command, channel):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text="What product would you like to search for?")
    while True:
        product, channel = parse_bot_commands(slack_client.rtm_read())
        if product:
            l = Locations()
            provinces = l.get_provinces()
            province_ids = l.get_province_ids()
            provinces_string = "\n"

            for province_no in provinces:
                provinces_string += str(province_no) + ": " + provinces[province_no] + "\n"

                # find province num
            slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text="Enter a province num from: " + provinces_string)        
            while True:
                province_num, channel = parse_bot_commands(slack_client.rtm_read())
                if province_num:
                    province_num = int(str(province_num))
                    print(province_num)
                    website = url(product, province_num, provinces, province_ids)

                    (product_name, product_price, link, date) = cheapest(website, product)
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=channel,
                        text="The cheapest " + product + " in " + provinces[province_num] + (
                        " is the \n" + product_name + "\n") +  (
                            "costing $" + str(product_price) + ", posted " + date + (
                                "\n" + "Here's the link: \n" + link))  
                    + "\nWould you like to save to save this to a database?")
                    while True:
                        save, channel = parse_bot_commands(slack_client.rtm_read())
                        if (save and save.lower().startswith("y")):
                            slack_client.api_call(
                                "chat.postMessage",
                                channel=channel,
                                text="Give the name of the db file to save to (if it doesn't exist it will create one for you)")                               
                            while True:
                                table_name, channel = parse_bot_commands(slack_client.rtm_read())
                                if (table_name):
                                    db(product_name, product_price, provinces[province_num], link, date, "databases/" + table_name)
                        else:
                            break
                            
                        
                        time.sleep(RTM_READ_DELAY)
                     
                time.sleep(RTM_READ_DELAY)
        time.sleep(RTM_READ_DELAY)
    time.sleep(RTM_READ_DELAY)    

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        # get the command
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command == "start":
                # start going through the sequence of commands
                
                slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text="Sure, would you like to *{}* or *{}*?".format("peek", "monitor"))
                
                while True:
                    command, channel = parse_bot_commands(slack_client.rtm_read())
                    if command == "peek":
                        peek(command, channel)
            time.sleep(RTM_READ_DELAY)
        '''
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
        '''