class Train:
    def __init__(self):
        self.wagons = []

    def __len__(self):
        return len(self.wagons)

    def add_wagon(self, new_wagon):
        self.wagons.append(new_wagon)
        return self

    def __str__(self):
        wagon_reprs = "-".join(str(wagon) for wagon in self.wagons[0:])
        return f"<=[HEAD]-{wagon_reprs}"
