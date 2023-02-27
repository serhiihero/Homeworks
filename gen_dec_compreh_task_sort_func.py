# Create a function that can return the squares of even elements for the range
# 0 to 1000000000 inclusive. The solution should work and not freeze your computer.

def even_num_filter_func():
    custom_generator = (x for x in range(0, 1000000001))
    for data in custom_generator:
        if data % 2 == 0:
            yield data ** 2


if __name__ == '__main__':
    for result in even_num_filter_func():
        print(result)
