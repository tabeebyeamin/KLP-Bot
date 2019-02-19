from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
# tbhsooting
from time import time

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
    # let the first object have the lowest price
    t0 = time()
    # find the first valid item
    first_found = False
    while (not first_found):
        container = page_soup.find('div', {'class': 'search-item regular-ad'})
        product = container.a.text.strip()
        page_soup.contents = page_soup.contents[page_soup.index(container)+1:]
        if givenproduct.lower() in product.lower():        
            cheapest_price = float(
                container.find('div', {"class":"price"}).text.replace('$',
                                                '').replace(',','').replace(' ', ''))
            cheapest_product = str(product)
            first_found = True
        
        
    
    # find the next result
    while (page_soup.find('div', {'class': 'search-item regular-ad'})):
        container = page_soup.find('div', {'class': 'search-item regular-ad'})
        product = container.a.text.strip()
        page_soup.contents = page_soup.contents[page_soup.index(container)+1:]
        if givenproduct.lower() in product.lower():
            price = container.find('div', {"class":"price"}).text            
            try:
                #print(price)
                # strip out the $ and ,            
                price = float(price.replace('$',
                                            '').replace(',','').replace(' ', ''))
                # change from unicode to string
                product = str(product)
                if (price < cheapest_price):
                    (cheapest_price, cheapest_product) = (price, product)
            except:
                pass
    
    return (cheapest_product, cheapest_price, time()-t0)


