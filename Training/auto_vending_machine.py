from random import random

def display_rows(products):
    """
    Neat display all our products row by row

    products: nested list of strings corresponding to products
    """

    for row in products:
        print(row)

def dispense_change(price, user_money):
    """
    Function to compute change for the user given
    a product price and money paid by the user.

    price: a floating point number corresponding to price of product
    user_money: a floating point number corresponding to user input
    """

    # check if user paid less than price
    if user_money < price:
        print("Hey! You owe us money!")

    # otherwise check if user paid the exact amount
    elif user_money == price:
        print("Nice, have a good life, you're done.")

    # else compute change owed to the user
    else:
        # first compute change owed in terms of cents
        user_money_cents = int(user_money*100)
        price_cents = int(price*100)
        change_in_cents = user_money_cents - price_cents

        # decompose cents in quarters, dimes, and pennies
        num_quarters = change_in_cents // 25
        remainder = change_in_cents % 25
        num_dimes = remainder // 10
        num_pennies = remainder % 10
        print("Num quarters", num_quarters)
        print("Num dimes", num_dimes)
        print("Num pennies", num_pennies)


def accept_money(price):
    """
    Function that uses a while loop to accept user money
    """

    price_cents = int(price*100)
    total_cents = 0

    # keep asking for user input until they provide enough money for the product
    while total_cents < price_cents:

        money = int(input("Give me money in quarters, 1 dollar, or 5 dollars: "))

        if money == 25 or money == 100 or money == 500:

            # randomly lose money with 50% probability... you probably don't actually want this
            # in the real world!!!
            if random() > 0.5:
                total_cents = total_cents + money
            else:
                print("Whoops, lost your money")

        else:
            print("Hey give me moneyz in a proper denomination")

    return total_cents / 100


if __name__ == "__main__":

    # nested list of products
    products = [["🍫", "🥤", "🍪"], 
                ["🍎", "🥠", "🧋"],
                ["🌯", "🥨", "🧀"]]

    # nested list of prices
    prices = [[1.12, 2, 1], 
              [0.5, 100, 5],
              [8, 1, 1]]

    # display the products
    print("Make a choice using row, col index notation")
    display_rows(products)
    
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))

    product_price = prices[row][col]

    print("Price of that is", product_price)

    user_money = accept_money(product_price)

    print("You paid", user_money)

    dispense_change(product_price, user_money)

    print("Here's your", products[row][col], "!")