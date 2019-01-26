from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# this is a function that takes a Canadacomputers url and finds the cheapest
# price on that url
def cheapest_price(my_url):
    '''(url) -> tuple of string and float
    This function takes a page url that has a list of products
    and finds the cheapest product on that page.
    REQ: The url must be a page url or else the program is unlikely
    to work.
    >>> cheapest_price('http://www.canadacomputers.com/index.php?cPath=21')
    'Cheapest product is $6.49, the Elephant WEM-1015 (PLUS) Rigid Mic
    Laser Mouse + Cable Clips, Black'
    '''
    # open up the connection, grab the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # do the html parsing
    page_soup = soup(page_html, "html.parser")
    # find all the items information 
    containers = page_soup.findAll('div', {'class': 'productarea'})

    # create an empty dictionary of monitors to pricers
    product_to_prices = {}
    # cycle through the containers
    for container in containers:
        # find the name of the model of the monitor
        product = container.p.text
        # extract the 3 possible prices and store them as lists
        price_1 = container.findAll('p',
                                    {"class":"price-ourprice price-final"})
        price_2 = container.findAll('p',
                                    {"class":"price-ir price-final redtxt"})
        price_3 = container.findAll('p',
                                    {"class":"price-final redtxt"})
        # add them together (if the price does not exist it won't add anything)
        # this will be a one element soup object
        text_price = price_1 + price_2 + price_3
        # extract the text from the first element of the soup list object
        price = text_price[0].text
        # strip out the $ and ,
        price = float(price.strip('$').replace(',',''))
        # map the product to the price
        product_to_prices[product] = price
    # find the cheapest price out of the recorded prices
    cheapest_price = min(product_to_prices.values())
    # now check the cheapest product
    for product in product_to_prices.keys():
        # strip the dollar sign from the price
        price = product_to_prices[product]
        # check if the value of the products is less than the previous lowest
        if (price == cheapest_price):
            # change the cheapest product to this one
            cheapest_product = product
    return (cheapest_product, cheapest_price)
