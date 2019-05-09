class Product:
    """
    A Product Listing item that has a price, name, date of the post and
    its url.
    """

    def __init__(self):
        self._price = None
        self._name = None
        self._date = None
        self._url = None

    def set_price(self, new_price):
        self._price = new_price

    def set_name(self, new_name):
        self._name = new_name

    def set_date(self, new_date):
        self._date = new_date

    def set_url(self, new_url):
        self._url = new_url


    """
    GETTERS
    """ 
    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

    def get_date(self):
        return self._date

    def get_url(self):
        return self._url 