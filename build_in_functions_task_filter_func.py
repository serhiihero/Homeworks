# Implement your realization of the function filter
from typing import Callable


def filter_for_allowed_types(iterable):
    filtered_data = []
    for data in iterable:
        if isinstance(data, (int, float)) and data < 5 and not isinstance(data, bool):
            filtered_data.append(data)
    return filtered_data


def custom_filter(callback: Callable, iterable):
    """
    Custom filter func which process data
    :param callback: allows to call needed func with diff types
    :param iterable: data which needs to be filtered
    """
    return callback(iterable)


if __name__ == '__main__':
    result = custom_filter(filter_for_allowed_types,
                           [2, 5, 6, 7, [1, 2, 3], ("One", "Two"), 22, "sate", True, 2.2, 5, 101,
                            {"name": "David", "age": 3}])
    print(result)
