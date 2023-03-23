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

    def write_file(self, new_data: str | int | float):
        if new_data != self.__result and new_data != '':
            self.__txt_writer.write(new_data)
            self.__is_actual = False
        else:
            print('Nothing to write.')

if __name__ == '__main__':
    txt_file = TxtProxyWriterReader('my_file.txt')
    print(txt_file.read_file())
    txt_file.write_file('')
    print(txt_file.read_file())
    txt_file.write_file('This text for write.')
    print(txt_file.read_file())

