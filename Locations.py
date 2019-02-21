class Locations:
    '''
    This class stores information about Locations available in Kijiji Canada
    '''
    def __init__(self):
        '''
        Default constructor
        '''
        # mapping of province numbers to province names
        self._provinces = {0: "Ontario",
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
        
        # mapping of province numbers to province ids
        self._province_ids = {0: "k0l9004",
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

    def get_provinces(self):
        '''
        Get mapping of province numbers to province names  
        '''
        return self._provinces
    
    def get_province_ids(self):
        '''
        Get mapping of province numbers to province ids 
        '''
        return self._province_ids