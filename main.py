from movie import Movie
from rental import Rental
from customer import Customer


def main():
    rental1 = Rental(
        Movie('Back to the Future', 2),
        4
    )

    rental2 = Rental(
        Movie('Office Space', 0),
        3
    )

    rental3 = Rental(
        Movie('The Big Lebowski', 1),
        5
    )

    customer = Customer('Joe Schmoe')

    customer.add_rental(rental1)
    customer.add_rental(rental2)
    customer.add_rental(rental3)

    print(customer.statement())

if __name__ == '__main__':
    main()
  

