# Implement your own all function

def custom_func(input_data):
    for element in input_data:
        if not bool(element):
            return False
    return True


if __name__ == '__main__':
    result = custom_func([1, 2, 3, 4])
    print(result)
    result = custom_func(["hello", "world", ""])
    print(result)
