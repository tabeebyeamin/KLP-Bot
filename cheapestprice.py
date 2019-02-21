from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

# this is a function that takes a Canadacomputers url and finds the cheapest
# price on that url
def cheapest_price(my_url, givenproduct):
    '''(url, string) -> (string, float, string, string)
    This function takes a kijiji page url that has a list of products
    and finds the cheapest product on that page.
    REQ: The url must be a kijiji page url or else the program is unlikely
    to work.
    >>> cheapest_price("https://www.kijiji.ca/b-ontario/gtx-1070/k0l9004")
    '''
    # open up the connection, grab the page

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # do the html parsing
    page_soup = soup(page_html, "html.parser")
    # find all the items information
    
    containers = page_soup.findAll('div', {'class': 'search-item regular-ad'})

    # create empty dicts of prices, urls and dates attributres
    product_to_prices = {}
    product_to_urls = {}
    product_to_dates = {}
    
    # cycle through the containers
    for container in containers:
        # find the name of the model of the product
        product = container.a.text.strip()
        if givenproduct.lower() in product.lower():
            
            # extract the price and store it
            # this used to be findAll
            price = container.find('div',
                                        {"class":"price"}).text
            # get the url of the product
            url = "https://www.kijiji.ca" + str(container.get('data-vip-url'))
            
            date = container.find('span',{"class": "date-posted"}).text
            
            # see if the price is valid
            try:
                # strip out the $ and ,            
                price = float(
                    price.replace('$', '').replace(',', '').replace(' ', ''))
                # change from unicode to string
                date = str(date)
                product = str(product)
                
                # map product's price, url and date
                product_to_prices[product] = price
                product_to_urls[product] = url
                product_to_dates[product] = date
            # otherwise skip it
            except:
                pass
    # find the cheapest price out of the recorded prices
    cheapest_price = min(product_to_prices.values())
    # now check the cheapest product
    for product in product_to_prices:
        # extract the price from price dict
        price = product_to_prices[product]
        # check if the value of the products is < the previous lowest
        if (price == cheapest_price):
            # change the cheapest product to this one
            cheapest_product = product
            cheapest_url = product_to_urls[product]
            cheapest_date = product_to_dates[product]

    # return name, price, url and date
    return (cheapest_product, cheapest_price, cheapest_url, cheapest_date)