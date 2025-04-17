from abc import ABC 

class Vehicle(ABC):
    speed = {
        'car' : 50,
        'bike' : 60,
        'cng' : 25,
    }

    def __init__(self, type, license_plate, rate):
        self.type = type
        self.license_plate = license_plate
        self.rate = rate

class Car(Vehicle):
    def __init__(self, type, license_plate, rate):
        super().__init__(type, license_plate, rate)

class Bike(Vehicle):
    def __init__(self, type, license_plate, rate):
        super().__init__(type, license_plate, rate)

