from writer import Writer


class TxtWriter(Writer):

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, new_data):
        with open(self.file_path, 'w') as file:
            if isinstance(new_data, str):
                text_container = file.write(new_data)
            else:
                text_container = file.write(str(new_data))
        return text_container
