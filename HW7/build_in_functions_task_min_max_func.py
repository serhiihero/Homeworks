# Implement your own implementation of function max and min
# (* additional argument amount of result, if you pass 2, function should return 2 max values from the list)
from typing import Callable


def custom_func(callback: Callable, *args):
    return callback(*args[0])


def func_to_filter_min_value(*args):
    list_to_compare = []
    for input_data in args:
        if len(list_to_compare) == 0:
            list_to_compare.append(input_data)
        elif len(list_to_compare) != 0 and input_data < list_to_compare[0]:
            list_to_compare.remove(list_to_compare[0])
            list_to_compare.append(input_data)
    return list_to_compare[0]


def func_to_filter_max_value(*args):
    list_to_compare = []
    for input_data in args:
        if len(list_to_compare) == 0:
            list_to_compare.append(input_data)
        elif len(list_to_compare) != 0 and input_data > list_to_compare[0]:
            list_to_compare.remove(list_to_compare[0])
            list_to_compare.append(input_data)
    return list_to_compare[0]


if __name__ == '__main__':
    data_to_be_sorted = [7.14, -1.12, 10.66, 55.5, 17, 4]
    data_to_be_sorted_1 = ["Denmark", "English", "French", "Italian"]
    result = custom_func(func_to_filter_min_value, data_to_be_sorted)
    print(result)
    result = custom_func(func_to_filter_max_value, data_to_be_sorted)
    print(result)
    result = custom_func(func_to_filter_min_value, data_to_be_sorted_1)
    print(result)
    result = custom_func(func_to_filter_max_value, data_to_be_sorted_1)
    print(result)
