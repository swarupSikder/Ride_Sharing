from abc import ABC, abstractmethod

class User:
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = initial_amount
        self.current_ride = None

    def display_profile(self):
        print(f'Rider : {self.name} and Email : {self.email}')

    def loadCash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print('Error')

    def updateLocation(self, current_location):
        self.current_location = current_location

    def requestRide(self, ride_sharing, destination):
        pass

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f'Driver Name : {self.name}')

    def accept_ride(self, ride):
        ride.set_driver(self)