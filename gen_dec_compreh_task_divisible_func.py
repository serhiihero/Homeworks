# Find all of the numbers from 1-1000 that are divisible by 7

def divisible_num_filter_func():
    custom_generator = (x for x in range(1, 1000))
    for data in custom_generator:
        if data % 7 == 0:
            yield data


if __name__ == '__main__':
    divisible_num_filter_func()
