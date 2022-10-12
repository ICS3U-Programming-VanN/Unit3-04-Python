#!/usr/bin/env python3
# Created by: Van Nguyen
# Created on: October 11, 2022
# This program asks the user to input an integer and
# then the program displays whether or not the integer is negative, positive or zero


def main():
    # Asks user to input a number
    user_integer = int(input("Enter an integer: "))

    # IF the user inputs zero
    if user_integer < 0:
        print(f"{user_integer} is a negative number.")

    # IF the user inputs a positive number
    elif user_integer > 0:
        print(f"{user_integer} is a positive number.")

    # IF the user inputs a negative number
    else:
        print(f"{user_integer} is just zero.")


if __name__ == "__main__":
    main()
