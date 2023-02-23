# Implement your own all function

def custom_func(input_data):
    for element in input_data:
        if not element:
            return False
    return True


if __name__ == '__main__':
    print(custom_func([1, 2, 3, 4]))
    print(custom_func(["hello", "world", ""]))
