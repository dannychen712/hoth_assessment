## Introduction

This example comes from the book Refactoring by Martin Fowler.

There are solutions to this problem readily available on the Internet, so please adhere to the honor system: don't cheat!

## Requirements

We use Python 3.12 in production, so feel free to use any appropriate language features that you see fit.

Feel free to include any external libraries or dependencies that you believe will add value to the project.

## Project

The project concerns movie rentals and customer billing statements.

There are 3 existing classes:

- **`Movie`** is composed of a title - `name` - and a pricing code - `price_code`.
- **`Rental`** is composed of a `Movie` - `movie` - and a duration - `days_rented`.
- **`Customer`** is composed of a name - `name` - and, optionally, a `Rental` collection / array - `rentals`.

The `Customer` class also contains a method - `statement()` - that prints a plain-text statement containing the customer's billing and loyalty information.

## Current State

The program can be run by `$ python3 main.py`.

This should be the output:

```
Rental Record for Joe Schmoe
        Back to the Future              3
        Office Space                    3.5
        The Big Lebowski                15
Amount owed is 21.5
You earned 4 frequent renter points

```

## Your Tasks

1. The business now requires billing statements in HTML - in addition to their current text output. The desired HTML output is shown below. Please implement HTML output (on a per-customer basis). You are welcome to use a library or package to improve upon the HTML output, but you should at least have the provided HTML output as your final result.
2. The business wants to change the movie classifications. They may, for example, wish to remove "Children's" or add a new classification called "SciFi". Then again, they may simply wish to change the algorithms for calculating frequent renter points. **In other words, the classification / pricing / points system needs to be more flexible.** (This task is intentionally open-ended.)

### HTML Output for Task #1

```
<h1>Rental Record for <em>Joe Schmoe</em></h1>
<ul>
    <li>Back to the Future - 3</li>
    <li>Office Space - 3.5</li>
    <li>The Big Lebowski - 15</li>
<ul>
<p>Amount owed is <em>21.5</em>
<p>You earned <em>4</em> frequent renter points!</p>
```

## Your Deliverables

1. Return your solution as a `.zip` or `.tgz` file.
2. Include a rough estimate of how much time you spent working on the assignment.
3. Also include any additional instructions / requirements for running your solution.
4. Finally, please feel free - though you're not required - to provide some "documentation" to justify any tradeoffs you might have made when writing the code and what implications those tradeoffs may have in the future - especially for the second "task" above.

## Response
1. Return your solution as a `.zip` or `.tgz` file: Done
2. I spent approximately 2.5 hours on this project
3. The way you run the code is the same `python main.py`, but now you need to do a `pip install -r requirements.txt` prior to install yattag html tools.
4. The main point of the refactor was to create a data structure "price_codes" in movie.py, and to move the price calculation to rental.py in order to clean up the concerns of customer.py. I am still not all the way happy with customer.py because I think that there is a distinct "order" concept that could be separated out. customer.py is still doing a lot of heavy lifting in terms of the statement logic.

In movie.py I added a dictionary called "price_codes" which attempts to add some consistency in how we represent the different rates and days. I have added a top level comment to describe this in movie.py. When you initialize a Movie object and pass in the price code it allows you to return a property "price_structure" which contains the base_rate, base_days, and subsequent_days. This is used in rental.py to calculate the rate per rental. I think its is much cleaner because you can add a new rate code with the aforementioned 3 data points to generate an accurate calculation in order to create any number of new movie rate types. This whole data structure would ideally be in a database and not just a hardcoded dictionary. 

Finally, the html is generated within customer.py with the yattag library. The naming convention is 
First_Last_%m_%d_%Y_%H:%M:%S.html with the date/time in strftime format.