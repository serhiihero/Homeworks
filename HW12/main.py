# Describe the Train object.
# The class must contain fields and a method for adding wagons (it is necessary to add objects,
# instances of the wagon class).
# Describe the class Wagon together with the train.
# The Wagon must contain a list of passengers and allow adding passengers.
# In the Wagon can be 10 passengers for example.
# When using the len function on a Wagon, I want to see the number of passengers.
# When using len on a train, I want to see a list of Wagons without a locomotive.
# Each wagon must have a number.
# When printing a wagon to the console, I want to see the following "[n]" where n is the number of the wagon.
# ***
# Implement a train print from task 2.
# When you print a train, wagons and a locomotive should be displayed in the console in the following format:
# <=[HEAD]-[1]-[2]-[3]-[4]-[...]-[n]-[n-1]

from class_train import Train
from class_wagon import Wagon

if __name__ == '__main__':
    train = Train()
    wagon_1 = Wagon(1)
    wagon_1.add_passenger('Alice')
    wagon_1.add_passenger('David')
    wagon_1.add_passenger('Charmine')
    print(f'How many passengers in the wagon {wagon_1}?\n\t{len(wagon_1)}')
    wagon_2 = Wagon(2)
    wagon_2.add_passenger('Emma')
    print(f'How many passengers in the wagon {wagon_2}?\n\t{len(wagon_2)}')
    wagon_3 = Wagon(3)
    wagon_3.add_passenger('Simon')
    wagon_3.add_passenger('Lemma')
    print(f'How many passengers in the wagon {wagon_3}?\n\t{len(wagon_3)}')
    train.add_wagon(wagon_1).add_wagon(wagon_2).add_wagon(wagon_3)
    print(f'How many wagons in the train?\n\t{len(train)}')
    print(train)
