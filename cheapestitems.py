from cheapestprice import cheapest_price as cheapest

def cheapest_product(my_url):
    '''(url) -> tuple of string and float
    This function takes a page url that has a list of products
    and finds the cheapest product on that page.
    REQ: The url must be a page url or else the program is unlikely
    to work.
    >>> cheapest_product('http://www.canadacomputers.com/index.php?cPath=21')
    'Cheapest product is $6.49, the Elephant WEM-1015 (PLUS) Rigid Mic
    Laser Mouse + Cable Clips, Black'
    '''
    # start with the base page
    (cheapest_product, cheapest_price) = cheapest(my_url)
    # set the default value for the index
    index = 2
    # set the default value for duplicate found
    duplicate_found = False
    # check every page for the product
    while (not duplicate_found):
        # add the extension to the url
        my_url += '&page='
        my_url += str(index)
        # input the new url into the function
        (new_product, new_price) = cheapest(my_url)
        # check to see if the lowest price item has been duplicated before
        if (new_product == cheapest_product):
            # if so, stop the loop
            duplicate_found = True
        # otherwise, check to see if the new price is the lowest
        elif (new_price < cheapest_price):
            # record the new price as the cheapest
            cheapest_price = new_price
            cheapest_product = new_product
        # increment the page number by 1
        index += 1
        print(cheapest_product)

    return (cheapest_product, cheapest_price)
    