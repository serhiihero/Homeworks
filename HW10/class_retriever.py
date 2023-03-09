from class_home_dog import HomeDog


class Retriever(HomeDog):

    def __init__(self, animal_type: str = None, habitat: str = None, food_preference: str = None,
                 wool_type: str = None, ability_help_blind: str = None):
        super().__init__(animal_type, habitat, food_preference, wool_type)
        self.__ability_help_blind = ability_help_blind

    @property
    def ability_help_blind(self):
        return self.__ability_help_blind

    @ability_help_blind.setter
    def ability_help_blind(self, change_ability_help_blind):
        self.__ability_help_blind = change_ability_help_blind

    @staticmethod
    def intro_retrievers():
        return 'Retrievers can help humans in a bunch of areas.'

    def eat(self, replacement: str = None):
        return f'I am {self.animal_type}, living in {self.habitat}, prefer to eat {self.food_preference} or {replacement} and my wool {self.wool_type}.\n' \
               f'Also I have {self.ability_help_blind}.'


if __name__ == '__main__':
    retriever = Retriever('retriever', 'human\'s home', 'meat', 'not adapted to the wild',
                          'an ability to help blind people')
    print(retriever.intro_retrievers())
    print(retriever.eat('cottage cheese'))
