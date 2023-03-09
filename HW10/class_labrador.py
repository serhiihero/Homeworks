from class_retriever import Retriever


class Labrador(Retriever):

    def __init__(self, animal_type: str = None, habitat: str = None, food_preference: str = None,
                 wool_type: str = None, ability_help_blind: str = None, smell_quality: str = None):
        super().__init__(animal_type, habitat, food_preference, wool_type, ability_help_blind)
        self.__smell_quality = smell_quality

    @property
    def smell_quality(self):
        return self.__smell_quality

    @smell_quality.setter
    def smell_quality(self, change_smell_quality):
        self.__smell_quality = change_smell_quality

    @staticmethod
    def intro_labradors():
        return 'Labradors can help humans in many areas.'

    def eat(self, replacement: str = None):
        return f'I am {self.animal_type}, living in {self.habitat}, prefer to eat {self.food_preference} or {replacement} and my wool {self.wool_type}.\n' \
               f'Also I have {self.ability_help_blind} and {self.smell_quality}.'


if __name__ == '__main__':
    labrador = Labrador('labrador', 'human\'s home', 'meat', 'not adapted to the wild',
                        'an ability to help blind people', 'unrivaled sense of smell')
    print(labrador.intro_labradors())
    print(labrador.eat('yummies'))
