class CustomMagicClass:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


if __name__ == '__main__':
    custom_magic_class = CustomMagicClass('Derek')
    print(custom_magic_class)
