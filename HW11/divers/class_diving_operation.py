from HW11.divers.interfaces.diver_interface import IDiver
from HW11.divers.interfaces.human_interface import IHuman


# Inheritance
# Abstraction
class DivingOperation(IDiver, IHuman):

    def __init__(self, name):
        # Hiding
        self.__name = name
        self.__human_activity = False
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self.__on_land = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # Polymorphism
    # Hiding
    def _wake_up(self):
        print(f'{self.__name} woke up.')
        self.__human_activity = True

    # Polymorphism
    # Hiding
    def _immersion(self):
        self._wake_up()
        print('I am going to immersion.')
        self.__z = -50
        self.__on_land = False

    # Polymorphism
    # Hiding
    def _move_to_the_point(self, x, y):
        self._immersion()
        print(f'I am diving into the depths z: {self.__z}')
        self.__x = x
        self.__y = y

    # Encapsulation
    def collect_treasures(self, x, y):
        self._move_to_the_point(x, y)
        print(f'I am going try to collect treasures at x: {x} and y: {y}.')
        self._sell_treasures()

    # Polymorphism
    # Hiding
    def _sell_treasures(self):
        print('Returning to the land.')
        self.__z = 0
        self.__on_land = True
        print('I am going to sell treasures.')
        self._sleep()

    # Polymorphism
    # Hiding
    def _sleep(self):
        print('I am going to sleep after hard work.')
        self.__human_activity = False

    def signal_of_distress(self, x, y, z):
        if z < -50:
            print(f'SOS!!! I need more oxygen cylinders at x: {x} and y: {y} and depth z: {z}.')
