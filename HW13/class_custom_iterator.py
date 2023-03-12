# Create an iterator that accepts a sequence and can iterate over values in a given range.
# CustomIterator(sequence, start_index, end_index)
from random import randint


class CustomIterator:

    def __init__(self, sequence: int = None, start_position: int = None, end_position: int = None):
        self._sequence = sequence
        self._start_position = start_position
        self._end_position = end_position
        self._current_position = start_position

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_position < self._end_position:
            value = self._sequence[self._current_position]
            self._current_position += 1
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
