from yattag import Doc, indent
from datetime import datetime

class Customer:
    def __init__(self, name):
        self._name = name
        self.rentals = []
        self.frequent_renter_points = 0

    @property
    def name(self):
        return self._name

    def add_rental(self, rental):
        self.rentals.append(rental)
    
    def statement(self):
        """
        Customer statement, this method kind of serves as an "order" object. If time allowed I would
            probably like to separate out the "order" from the customer, but the "rentals" would persist
            to show how many days are left, late status, amount owed, etc.

        If "order" was separated out we would also have a better time generating results in any format,
            not just in a string that is lightly manipulated by code.
        """        
        total_amount = 0
        frequent_renter_points = 0
        result = f'Rental Record for {self.name}\n'

        # Interspersed html tagging, because I need the same data from the results text
        doc, tag, text = Doc().tagtext()
        with tag('h1'):
            text('Rental Record for ')
            with tag('em'):
                text(self.name)


        with tag('ul'):
            for rental in self.rentals:             
                current_amount = 0
                current_amount = rental.calculate_rate()
                frequent_renter_points += rental.calculate_frequent_rental_points()
                total_amount += current_amount
                result += "\t" + rental.movie.name.ljust(30) + "\t" + str(current_amount) + "\n"

                with tag('li'):
                    text(f"{rental.movie.name} - {current_amount}")
            
        result += f'Amount owed is {total_amount}\n'
        result += f'You earned {frequent_renter_points} frequent renter points\n'


        with tag('p'):
            text(f"Amount owed is ")
            with tag('em'):
                text(total_amount)

        with tag('p'):
            text(f"You earned ")
            with tag('em'):
                text(frequent_renter_points)
            text(" frequent renter points!")
        filename = f"{self.name.replace(' ', '_')}_{datetime.now().strftime('%m_%d_%Y_%H-%M-%S')}.html"
        with open(filename, 'w') as file:
            file.write(indent(doc.getvalue()))

        return result
