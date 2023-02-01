# Write a function is_prime that takes 1 argument - a number from 2 to 1000,
# and returns True if it is a prime number, and False otherwise.

def is_prime(number_checker: int) -> int:
    if 2 <= number_checker <= 1000:
        return True
    return False


if __name__ == '__main__':
    print(is_prime(number_checker=1))
    print(is_prime(number_checker=2))
    print(is_prime(number_checker=555))
    print(is_prime(number_checker=1000))
    print(is_prime(number_checker=1001))
