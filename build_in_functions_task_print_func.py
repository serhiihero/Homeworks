# Implement your own print function.
# It should work on all operating systems.
# You can't use build-in print function
import sys


def print_func(*args, **kwargs):
    return sys.stdout.write(str(*args, **kwargs))


if __name__ == '__main__':
    print_func('Hello World')
