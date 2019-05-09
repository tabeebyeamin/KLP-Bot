class Url:
    """
    A Kijiji Product search Url object consists of the following: 
    product_name, province_num, provinces, province_ids
    """

    def __init__(self):
        self._product_name = None
        self._province_num = None
        self._provinces = None
        self._province_ids = None

    def set_product_name(self, product_name):
        self._product_name = product_name

    def set_province_num(self, province_num):
        self._province_num = province_num

    def set_provinces(self, provinces):
        self._provinces = provinces

    def set_province_ids(self, province_ids):
        self._province_ids = province_ids

    def generate(self):
        # generate the link for the province part
        provincehtml = self._provinces[self._province_num].lower().replace(
            " ", "-")
        # generate the link for the product part
        producthtml = self._product_name.lower().replace(" ", "-")
        # generate the province id portion
        province_id = self._province_ids[self._province_num]

        # put it together and return it
        website = "https://www.kijiji.ca/b-" + (
            provincehtml + "/" + producthtml + "/" + province_id)
        return website
