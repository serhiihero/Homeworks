from class_animal import Animal
from abc import abstractmethod


class Mammal(Animal):

    def __init__(self, animal_type: str = None, habitat: str = None):
        super().__init__(animal_type)
        self.__habitat = habitat

    @property
    def habitat(self):
        return self.__habitat

    @habitat.setter
    def habitat(self, reassigned_habitat):
        self.__habitat = reassigned_habitat

    @abstractmethod
    def eat(self, replacement: str = None):
        pass
