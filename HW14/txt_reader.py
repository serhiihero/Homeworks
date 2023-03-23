from reader import Reader


class TxtReader(Reader):

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            text_container = file.readlines()
        return text_container
