# Please describe an object as we did with Helicopter.
# Using all OOP postulates. Add comments where you use postulate.
# For example:
# # Inheritance
# class SomeObject(Other_Object)
# def __init__()....
# # hiding
# self.__parameter ...
# # encapsulation
# @property

from class_diving_operation import DivingOperation

if __name__ == '__main__':
    diving_operation = DivingOperation('Peter')
    diving_operation.collect_treasures(150, 150)
    diving_operation.signal_of_distress(150, 150, -51)
