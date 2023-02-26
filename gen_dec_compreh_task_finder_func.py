# Find all of the numbers from 1-1000 that have a 3 in them

def divisible_num_filter_func():
    custom_generator = (x for x in range(1, 1000))
    for data in custom_generator:
        if '3' in str(data):
            yield data


if __name__ == '__main__':
    divisible_num_filter_func()
