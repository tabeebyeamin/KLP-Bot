from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

# this is a function that takes a Canadacomputers url and finds the cheapest
# price on that url
def cheapest_price(my_url, givenproduct):
    '''(url) -> (string, float)
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
    containers = page_soup.findAll('div', {'class': 'search-item regular-ad'})
    
    #print(type(containers))
    # print(len(containers))

    # create an empty dictionary of monitors to pricers
    product_to_prices = {}
    # cycle through the containers
    for container in containers:
        # find the name of the model of the monitor
        product = container.a.text.strip()
        if givenproduct.lower() in product.lower():
            # print(product)
            
            # extract the possible prices and store them as a list
            # this used to be findAll
            price_1 = container.find('div',
                                        {"class":"price"})
            
            # extract the text from the first element of the soup list object
            # this used to be price_1[0]
            price = price_1.text
            # see if the price is valid
            try:
                #print(price)
                # strip out the $ and ,            
                price = float(price.replace('$',
                                            '').replace(',','').replace(' ', ''))
                # change from unicode to string
                product = str(product)
                product_to_prices[product] = price
                # find the cheapest price out of the recorded prices
                cheapest_price = min(product_to_prices.values())
                # now check the cheapest product
                for product in product_to_prices:
                    # strip the dollar sign from the price
                    price = product_to_prices[product]
                    # check if the value of the products is < the previous lowest
                    if (price == cheapest_price):
                        # change the cheapest product to this one
                        cheapest_product = product    
            # otherwise skip it
            except:
                pass
                
    return (cheapest_product, cheapest_price)