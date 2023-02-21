# Implement your realization of the function filter
from typing import Callable

filtered_data = []


def filter_for_allowed_types(iterable):
    for data in iterable:
        allowed_types = isinstance(data, (str, int, float))
        if allowed_types:
            filtered_data.append(data)


def custom_filter(callback: Callable, iterable):
    """
    Custom filter func which process data
    :param callback: allows to call needed func with diff types
    :param iterable: data which needs to be filtered
    """
    return callback(iterable)


if __name__ == '__main__':
    custom_filter(filter_for_allowed_types,
                  [2, 5, 6, 7, [1, 2, 3], ("One", "Two"), 22, "sate", True, 2.2, 5, 101,
                   {"name": "David"}])
    print(filtered_data)
