'''
KIJIJI Lowest Price Script
Author: Tabeeb Yeamin - https://github.com/tabeebyeamin/

Usage: Give an item and a location and find the lowest price item listing
on Kijiji within 2 seconds.

Complete:
- Searching Lowest Price in any province
- Saving results to database
- Interactive Slack Bot Option

Left To Do:
- Narrowing Price by City
- Adding a min price flag so that you can remove false listing that you aren't
looking for
- Storing to a default database
- Searching for products in Quebec is glitchy, might be because of the accents
or language difference?
- A GUI, maybe on the web
'''

from Locations import Locations
from Product import Product
from Url import Url
from cheapestprice import cheapest_price as cheapest
from sql import add_to_table as db


if (__name__ == "__main__"):
    # set the loop to run by default
    loopcond = True
    while (loopcond):
        # first arg is the product name
        product = input("Enter a product: ")

        # get the locations and location ids
        l = Locations()
        provinces = l.get_provinces()
        province_ids = l.get_province_ids()

        # generate a string of provinces to prompt user with
        provinces_string = "\n"
        for province_no in provinces:
            provinces_string += str(province_no) + ": " + (
                provinces[province_no] + "\n")

        # second arg is the province number
        province_num = input(
            "Enter a province number from:" + provinces_string)

        # generate the kijiji url
        websiteObject = Url()

        websiteObject.set_product_name(product)
        websiteObject.set_province_num(province_num)
        websiteObject.set_provinces(provinces)
        websiteObject.set_province_ids(province_ids)

        website = websiteObject.generate()

        # webscrape the product from the website
        cheapest_product = cheapest(website, product)

        # get the info
        product_name = cheapest_product.get_name()
        product_price = cheapest_product.get_price()
        product_url = cheapest_product.get_url()
        product_date = cheapest_product.get_date()

        # output the information
        print("The cheapest " + product + " in " + provinces[province_num] + (
            " is the \n" + product_name + "\n") + (
            "costing $" + str(product_price) + ", posted " + product_date + (
                "\n" + "Here's the product_url: \n" + product_url)))

        # prompt user if they want to save to a database
        save = input("Would you like to save this info to a database? Y/N\n")

        # Yes is any response that starts with a y/Y
        if (save.lower().startswith("y")):
            table_name = input(
                "Name of database you would like to store to?\n" + (
                    "(If it doesn't exist it will create the db file for you)\n"))
            # save to database
            db(product_name, product_price,
               provinces[province_num], product_url, product_date, table_name)

        # prompt user to run the program again
        run_again = input("run again? Y/N \n")
        # if they said anything but yes, stop
        loopcond = run_again.lower().startswith("y")
