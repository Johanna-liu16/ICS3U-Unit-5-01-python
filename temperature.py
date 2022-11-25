#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Nov 2022
# This program converts temperature

import random


def fahrenheit():

    # input
    print("This program converts celsius to fahrenheit.")
    str_cel = input("Enter degrees for celsius: ")

    # process
    try:
        int_cel = int(str_cel)
        fahrenheit = (9 / 5) * int_cel + 32
        print("{0}°C is equal to {1}°F.".format(int_cel, fahrenheit))
    except ValueError:
        print("Invalid integer")
    finally:
        print("Thanks for playing")
    # output

    print("\nDone.")


def main():
    # this function calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
