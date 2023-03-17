class Wagon:
    def __init__(self, wagon_number):
        self.__passengers = []
        self.__wagon_number = wagon_number

    def __len__(self):
        return len(self.__passengers)

    def add_passenger(self, passenger):
        if len(self.__passengers) >= 10:
            raise ValueError('Not more 10 passengers for each wagon.')
        self.__passengers.append(passenger)

    def __str__(self):
        return f"[{self.__wagon_number}]"
