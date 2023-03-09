# Describe mammals using principles from the lesson. You should implement different fields and methods.
# For example: Animals -> mammals -> flying mammals-> Bird -> Eagle
# Minimum 3 chains should be implemented
# Classes should be in different modules. You should have at least 5 different classes.
from abc import ABC


class Animal(ABC):

    def __init__(self, animal_type: str = None):
        self.__animal_type = animal_type

    @property
    def animal_type(self):
        return self.__animal_type

    @animal_type.setter
    def animal_type(self, new_animal_type):
        self.__animal_type = new_animal_type
