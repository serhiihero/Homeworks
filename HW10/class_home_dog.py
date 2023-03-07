from class_dog import Dog


class HomeDog(Dog):

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
    def intro_home_dogs_nature():
        return 'Home dogs love humans.'

    def eat(self, replacement: str = None):
        return f'I am {self.animal_type}, living in {self.habitat}...\n' \
               f'and prefer {self.food_preference} or {replacement} and my wool is {self.wool_type}.'


if __name__ == '__main__':
    homedog = HomeDog('home dog', 'dog house', 'meat', 'not adapted to the wild')
    print(homedog.intro_home_dogs_nature())
    print(homedog.eat('dog food'))
