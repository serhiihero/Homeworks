# Create an iterator that accepts a sequence and can iterate over values in a given range.
# CustomIterator(sequence, start_index, end_index)
from random import randint


class CustomIterator:

    def __init__(self, sequence, start_index: int = None, end_index: int = None):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index
        self.__current_position = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_position < self.__end_index:
            value = self.__sequence[self.__current_position]
            self.__current_position += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    list_of_data = []
    for input_item in range(1, 30):
        list_of_data.append(randint(1, 100))
    custom_iterator = CustomIterator(list_of_data, 2, 10)
    iterated_list = []
    for input_item in custom_iterator:
        iterated_list.append(input_item)
    print(list_of_data)
    print(iterated_list)
