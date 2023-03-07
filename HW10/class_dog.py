from class_mammal import Mammal


class Dog(Mammal):

    def __init__(self, animal_type: str = None, habitat: str = None, food_preference: str = None):
        super().__init__(animal_type, habitat)
        self.__food_preference = food_preference

    @property
    def food_preference(self):
        return self.__food_preference

    @food_preference.setter
    def food_preference(self, change_food_preference):
        self.__food_preference = change_food_preference

    @staticmethod
    def intro_dogs_nature():
        return 'We are so different: hunters or homebody.'

    def eat(self, replacement: str = None):
        return f'I am {self.animal_type}, living in {self.habitat} and prefer {self.food_preference} or {replacement}.'


if __name__ == '__main__':
    dog = Dog('dog', 'different places', 'meat')
    print(dog.intro_dogs_nature())
    print(dog.eat('anything that can find'))
