# Implement your own implementation of function max and min
# (* additional argument amount of result, if you pass 2, function should return 2 max values from the list)
from typing import Callable

filtered_min_list = []
filtered_max_list = []


def custom_min_numbers(user_data):
    for input_data in user_data:
        if len(filtered_min_list) == 0:
            filtered_min_list.append(input_data)
        elif len(filtered_min_list) != 0 and input_data < filtered_min_list[0]:
            filtered_min_list.remove(filtered_min_list[0])
            filtered_min_list.append(input_data)


def custom_min_str(user_data):
    for input_data in user_data:
        if len(filtered_min_list) == 0:
            filtered_min_list.append(input_data)
        elif len(filtered_min_list) != 0 and input_data < filtered_min_list[0]:
            filtered_min_list.remove(filtered_min_list[0])
            filtered_min_list.append(input_data)


def custom_min_func(custom_min_numbers: Callable, custom_min_str: Callable, user_data):
    for input_data in user_data:
        if isinstance(input_data, (int, float)):
            return custom_min_numbers(user_data)
        elif isinstance(input_data, str):
            return custom_min_str(user_data)


def custom_max_numbers(user_data):
    for input_data in user_data:
        if len(filtered_max_list) == 0:
            filtered_max_list.append(input_data)
        elif len(filtered_max_list) != 0 and input_data > filtered_max_list[0]:
            filtered_max_list.remove(filtered_max_list[0])
            filtered_max_list.append(input_data)


def custom_max_str(user_data):
    for input_data in user_data:
        if len(filtered_max_list) == 0:
            filtered_max_list.append(input_data)
        elif len(filtered_max_list) != 0 and input_data > filtered_max_list[0]:
            filtered_max_list.remove(filtered_max_list[0])
            filtered_max_list.append(input_data)


def custom_max_func(custom_max_numbers: Callable, custom_max_str: Callable, user_data):
    for input_data in user_data:
        if isinstance(input_data, (int, float)):
            return custom_max_numbers(user_data)
        elif isinstance(input_data, str):
            return custom_max_str(user_data)


if __name__ == '__main__':
    custom_min_func(custom_min_numbers, custom_min_str, [7.14, -1.12, 7.66])
    print(filtered_min_list)
    custom_max_func(custom_max_numbers, custom_max_str, ["Denmark", "English", "French", "Italian"])
    print(filtered_max_list)
