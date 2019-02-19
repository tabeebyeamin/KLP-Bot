from Locations import Locations
from url_parser import url_parser as url
from cheapestprice import cheapest_price as cheapest
from sql import add_to_table as db


if (__name__ == "__main__"):
    loopcond = True

    while (loopcond):
        # first arg
        product = input("enter a product: ")       
        
        l = Locations()
        provinces = l.get_provinces()
        province_ids = l.get_province_ids()
        
        
        provinces_string = "\n"
        for province_no in provinces:
            provinces_string += str(province_no) + ": " + provinces[province_no] + "\n"
        
        # second arg
        province_num = input("enter a province number from:" + provinces_string)
        
        website = url(product, province_num, provinces, province_ids)
        
        
        (product_name, product_price, link, date) = cheapest(website, product)
        
        print("The cheapest " + product + " in " + provinces[province_num] + (
            " is the \n" + product_name + "\n") +  (
            "costing $" + str(product_price) + ", posted " + date + (
                "\n" + "Here's the link: \n" + link)))
        
        save = input("Would you like to save this info to a database? Y/N\n")
        
        if (save.lower().startswith("y")):
            table_name = input("Name of database you would like to store to?\n(If it doesn't exist it will create the db file for you)\n")
            db(product_name, product_price, provinces[province_num], link, date, table_name)
            
        run_again = input("run again? Y/N \n")
        # if they said anything but yes, stop
        loopcond = run_again.lower().startswith("y")