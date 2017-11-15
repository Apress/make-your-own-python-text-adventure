class Vehicle:
    def __init__(self):
        raise NotImplementedError("You must use a subclass.")


class Motorcycle(Vehicle):
    def __init__(self):
        self.wheels = 2


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
