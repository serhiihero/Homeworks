# Implement your own implementation of the function map
from typing import Callable


def mapper(iterable):
    sorted_list = []
    for data in iterable:
        if isinstance(data, str):
            sorted_list.append(str(data).upper())
    return sorted_list


def custom_map(callback: Callable, iterable):
    """
    Custom map func which process data
    :param callback: allows to call needed func with diff types
    :param iterable: data which needs to be filtered
    """
    if len(iterable) > 0:
        return callback(iterable)


if __name__ == '__main__':
    data_to_be_sorted = ["Suzanna", "jUlIa", "Kate", 55]
    result = custom_map(mapper, data_to_be_sorted)
    print(result)
