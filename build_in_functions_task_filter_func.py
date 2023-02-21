# Implement your realization of the function filter

filtered_data = []


def filter_func(data_to_filter):
    """
    Function which allows to filter data
    :param data_to_filter: incoming data which have to be filtered
    :return:
    """
    for iterable_data in data_to_filter:
        if isinstance(iterable_data, (float, int, bool, str)):
            filtered_data.append(iterable_data)


if __name__ == '__main__':
    filter_func([2, 5, 6, 7, [1, 2, 3], ("One", "Two"), 22, "sate", True, 2.2, 5, 101, {"name": "David"}])
    print(filtered_data)
