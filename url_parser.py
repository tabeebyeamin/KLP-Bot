from cheapestprice import cheapest_price as cheapest
def url_parser():
    '''
    Asks the user for a province/city, product
    '''
    provinces = {0: "Ontario",
                 1: "Quebec",
                 2: "British Columbia",
                 3: "Alberta",
                 4: "Sasketchewan",
                 5: "Manitoba",
                 6: "Newfoundland",
                 7: "New Brunswick",
                 8: "Nova Scotia",
                 9: "Prince Edward Island",
                 10: "Yukon Terrorities",
                 11: "Northwest Territories",
                 12: "Nunavut"}
    provinces_string = "\n"
    for province_no in provinces:
        provinces_string += str(province_no) + ": " + provinces[province_no] + "\n"
    product = input("enter a product: ")
    province_num = input("enter a province number from:" + provinces_string)
    
    provincehtml = provinces[province_num].lower().replace(" ","-")
    producthtml = product.lower().replace(" ", "-")
    
    #print(provincehtml)
    #print(producthtml)
    provinceids = {0: "k0l9004",
                 1: "k0l9001",
                 2: "k0l9007",
                 3: "k0l9003",
                 4: "k0l9009",
                 5: "k0l9006",
                 6: "k0l9008",
                 7: "k0l9005",
                 8: "k0l9002",
                 9: "k0l9011",
                 10: "k0l1700104",
                 11: "k0l1700103",
                 12: "k0l1700105"}
    provinceid = provinceids[province_num]
    
    website = "https://www.kijiji.ca/b-" + (
        provincehtml + "/" + producthtml + "/" + provinceid)
    return cheapest(website)