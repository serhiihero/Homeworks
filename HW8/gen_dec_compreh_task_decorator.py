# Create a decorator that prints to the console the name of the function that was called.
# The function should work as intended.
# For example, create a pair of functions for the arithmetic operations of summation and multiplication.
# When calling these functions, the result of the operation must be returned and the name of the function
# that was called must be displayed in the console with the result. Small hint (__name__)

def main_func_of_processing(func):
    def nested(*args, **kwargs):
        returned_value = func(*args, **kwargs)
        print(f"Name of the called function: {func.__name__}. Result: {returned_value}")
        return returned_value

    return nested


@main_func_of_processing
def sum_two_numbers(first_input_data: int, second_input_data: int) -> int:
    operation_result = first_input_data + second_input_data
    return operation_result


@main_func_of_processing
def multiply_two_numbers(first_input_data: int, second_input_data: int) -> int:
    operation_result = first_input_data * second_input_data
    return operation_result


if __name__ == '__main__':
    multiply_two_numbers(1, 5)
