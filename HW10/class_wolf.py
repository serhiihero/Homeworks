from class_dog import Dog


class Wolf(Dog):

    def __init__(self, animal_type: str = None, habitat: str = None, food_preference: str = None,
                 wool_type: str = None):
        super().__init__(animal_type, habitat, food_preference)
        self.__wool_type = wool_type

    @property
    def wool_type(self):
        return self.__wool_type

    @wool_type.setter
    def wool_type(self, change_wool_type):
        self.__wool_type = change_wool_type

    @staticmethod
    def intro_wolfs_nature():
        return 'Wolfs love to hunt and eat any type of meat.'

    def eat(self, replacement: str = None):
        return f'I am {self.animal_type}, living in {self.habitat}...\n' \
               f'and prefer {self.food_preference} or {replacement} and my wool is {self.wool_type}.'


if __name__ == '__main__':
    wolf = Wolf('wolf', 'forest', 'wild animal\'s meat', 'adapted to the wild')
    print(wolf.intro_wolfs_nature())
    print(wolf.eat('any other meat'))
