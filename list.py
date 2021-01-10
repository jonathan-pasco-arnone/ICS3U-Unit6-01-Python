#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: January 2021
# This program uses a list/array

import random


def main():
    # This function generates 10 random numbers and displays them

    numbers = []
    sum_of_numbers = 0

    print("The following is 10 randomly generated numbers"
          " stored in the same variable.")
    print("")

    for loop_counter in range(0, 10):
        a_single_random_number = random.randint(0, 100)
        numbers.append(a_single_random_number)

    for loop_counter in range(0, 10):
        print("Random number {0}: {1}".format(loop_counter + 1,
                                              numbers[loop_counter]))
        sum_of_numbers = sum_of_numbers + numbers[loop_counter]

    print("")
    print("The sum is {0} (this is the sum of the "
          "random numbers which will be "
          "used to test if the average"
          " is correct or not)".format(sum_of_numbers))
    print("")
    average = sum_of_numbers / 10
    print("The average is {0}".format(average))


if __name__ == "__main__":
    main()
