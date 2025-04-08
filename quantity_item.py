#!/usr/bin/env python3
# Created by: Adwok Adiebo
# Created on: April 7th, 2025
# This program asks the user for the quantity of
# items purchased and calculates the cost with tax and a
# 10 % discount if total cost is > $ 1000.


def main():
    # The code below is the initial greeting.
    print("Hello and Welcome to Adwok's shop!")

    # The HST is the tax taken when the user gives a certain input
    HST = 13 / 100

    # The discount is offered when
    # total quantity of items $1000 before tax.
    DISCOUNT = 10 / 100

    # We have to ask the user for the quantity of items needed.
    quantity_as_string = input("Please enter the quantity of items: ")

    try:
        # We convert the quantity to an integer.
        quantity = int(quantity_as_string)

        # find the total cost = quantity * 100.
        total_cost = quantity * 100

        # find the tax = HST * totalCost.
        tax = HST * total_cost

        # find the discount = discount * totalCost.
        discount = DISCOUNT * total_cost

        if total_cost > 1000:

            # find the finalPrice = totalCost - discount + tax.
            final_price = total_cost - discount + tax

            # Display the final price
            print(f"The final price is ${final_price}")

        if total_cost < 1000:

            # find the final price = totalCost + tax.
            final_price = total_cost + tax

            # Display the final price.
            print(f"The final price is ${final_price}")
            print("")

    except:
        # When the user enters an unknown value it is invalid.
        print("Please enter a valid quantity.")

    finally:
        # Once everything is executed the above code will be displayed.
        print("Thank you and have a great day.")
        print("")


if __name__ == "__main__":
    main()
