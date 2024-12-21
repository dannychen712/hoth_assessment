class Movie:

    """
    Price structure with the key being the price code. New price codes just create
    a new key and determine the base_rate, base_days, and subsequent_days.
    In the future this should be in a database.

    base_rate: This determines initial cost to rent
    base_days: How many days of rentals the initial cost covers
    subqequent_days: Rate for subsequent days.
    """

    price_codes = {0: {"base_rate": 2, "base_days": 2, "subsequent_days": 1.5},
                   1: {"base_rate": 3, "base_days": 1, "subsequent_days": 3},
                   2: {"base_rate": 1.5, "base_days": 3, "subsequent_days": 1.5}
                   }
    

    def __init__(self, name, price_code):
        self._name = name
        self._price_code = price_code
        self._price_structure = self.price_codes[price_code]

    @property
    def name(self):
        return self._name
    
    @property
    def price_code(self):
        return self._price_code
    
    @property
    def price_structure(self):
        return self._price_structure