# Implement your own implementation of the function map
from typing import Callable

numbers = [20, 50, 600, 700, [1, 2, 3], ("One", "Two"), 22, "543", True, 2.2, 500.5, 101,
           {"name": "David"}]
filtered_data = []


def mapper(iterable):
    for data in iterable:
        allowed_float = isinstance(data, float)
        allowed_int = isinstance(data, int)
        allowed_str = isinstance(data, str)
        if allowed_int and data > 200:
            filtered_data.append(data + 2000)
        elif allowed_float:
            filtered_data.append(float(data) + 2000)
        elif allowed_str:
            filtered_data.append(int(data) + 2000)


def custom_map(callback: Callable, iterable):
    """
    Custom map func which process data
    :param callback: allows to call needed func with diff types
    :param iterable: data which needs to be filtered
    """
    if len(iterable) > 0:
        return callback(iterable)


if __name__ == '__main__':
    custom_map(mapper, numbers)
    print(numbers)
    print(filtered_data)
    print(numbers)
