class Rental:
    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented
        self._rental_cost = None
        self._frequent_rental_points = 0

    @property
    def movie(self):
        return self._movie

    @property
    def days_rented(self):
        return self._days_rented
    
    def calculate_rate(self):
        rate = 0
        price_structure = self.movie.price_structure

        # Initial rental base rate
        rate += price_structure['base_rate']

        # Calculate the subsequent rental days depending on cost and base days.
        if self._days_rented > price_structure["base_days"]:
            remaining_days = self._days_rented - price_structure["base_days"]
            rate += remaining_days * price_structure['subsequent_days']
        
        self.rental_cost = rate
        return self.rental_cost
    
    def calculate_frequent_rental_points(self):
        # Always add one frequent rental point per movie
        self._frequent_rental_points += 1
        
        # For high value movies, add one more frequent rental point if rented for more than a day.
        # If there were more consistent rules around this then move it to the price_structure
        # in the movie model.
        if self.movie.price_code == 1 and self._days_rented > 1:
            self._frequent_rental_points += 1
        
        return self._frequent_rental_points