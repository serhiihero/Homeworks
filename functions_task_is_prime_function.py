# Write a function is_prime that takes 1 argument - a number from 2 to 1000,
# and returns True if it is a prime number, and False otherwise.

import math


def is_prime(number_checker: int):
    if 2 <= number_checker <= 1000:
        for i in range(2, int(math.sqrt(number_checker)) + 1):
            if (number_checker % i) == 0:
                return False
        return True
    else:
        print('Please enter number from 2 to 1000')


if __name__ == '__main__':
    is_prime(number_checker=2)
