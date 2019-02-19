
def url_parser(product, province_num, provinces, province_ids):
    '''
    Asks the user for a province/city, product
    '''
    
    #print(provincehtml)
    #print(producthtml)
        
    provincehtml = provinces[province_num].lower().replace(" ","-")
    producthtml = product.lower().replace(" ", "-")
    
    province_id = province_ids[province_num]
    
    
    website = "https://www.kijiji.ca/b-" + (
        provincehtml + "/" + producthtml +  "/" + province_id)
    return website
    