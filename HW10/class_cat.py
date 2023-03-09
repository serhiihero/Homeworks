from class_mammal import Mammal


class Cat(Mammal):

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
    def intro_cats_nature():
        return 'Cats are homebody and love themselves'

    def eat(self, replacement: str = None):
        return f'I am {self.animal_type}, living in {self.habitat} and prefer {self.food_preference} or {replacement}'


if __name__ == '__main__':
    cat = Cat('cat', 'home', 'fish')
    print(cat.intro_cats_nature())
    print(cat.eat('mouse'))
