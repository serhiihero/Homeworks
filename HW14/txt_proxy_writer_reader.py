from txt_reader import TxtReader
from txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self, new_data):
        if not isinstance(new_data, (str, int, float)):
            raise TypeError("String, int or float expected for such writer.")
        else:
            text_container = self.__txt_reader.read()
            if new_data in text_container:
                raise ValueError(f"This text is already exists in {self.__txt_reader.file_path}.")
            else:
                self.__result = self.__txt_writer.write(new_data)
                self.__is_actual = True
                return self.__result


if __name__ == '__main__':
    txt_writer = TxtProxyWriterReader('my_file.txt')

    txt_writer.write_file('WhatS is Lorem Ipsum?')
    txt_writer.write_file('What is Lorem Ipsum?')
    txt_writer.write_file('WhatS is Lorem Ipsum?')
    txt_writer.write_file(123)
    txt_writer.write_file(3.14)
    txt_writer.write_file('What is Lorem Ipsum? Lorem Ipsum is simply.')
    txt_writer.write_file('What is Lorem Ipsum? Lorem Ipsum is simply.')
