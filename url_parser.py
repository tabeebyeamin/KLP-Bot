def url_parser(product, province_num, provinces, province_ids):
    ''' (str, int, dict, dict) -> str
    Takes in a product name, a province number from a mapping of number
    of provinces and provice_ids dictionaries.
    
    REQ: product string must have proper spacing. i.e it cannot start or end
    with a space and name have a maximum of 1 space between words.
    
    >>> import Locations
    >>> l = Locations()
    >>> provinces = l.get_provinces()
    >>> province_ids = l.get_province_ids()
    >>> url_parser("gtx 1070", 0, provinces, province_ids)
    "https://www.kijiji.ca/b-ontario/gtx-1070/k0l9004
    '''
    # generate the link for the province part        
    provincehtml = provinces[province_num].lower().replace(" ","-")
    # generate the link for the product part
    producthtml = product.lower().replace(" ", "-")
    # generate the province id portion 
    province_id = province_ids[province_num]
    
    # put it together and return it
    website = "https://www.kijiji.ca/b-" + (
        provincehtml + "/" + producthtml +  "/" + province_id)
    return website
    