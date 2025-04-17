from abc import ABC, abstractmethod
from ride import Ride, RideRequest, RideMatch, RideSharing

class User(ABC):
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

    def requestRide(self, ride_sharing, destination, vehicle_type):
        ride_req = RideRequest(self, destination)
        ride_matching = RideMatch(ride_sharing.drivers)
        ride = ride_matching.find_drivers(ride_req, vehicle_type)
        ride.rider = self
        self.current_ride = ride 
        print('Yes! I got a ride!')

    def show_current_ride(self):
        print('\n---------(Ride Details)-----------')
        print(f'Rider: {self.name}')
        print(f'Driver: {self.current_ride.driver.name}')
        print(f'Selected Car: {self.current_ride.vehicle.vehicle_type}')
        print(f'Start Location: {self.current_ride.start_location}')
        print(f'End Location: {self.current_ride.end_location}')
        print(f'Total Cost: {self.current_ride.estimated_fare}')

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f'Driver Name : {self.name}')

    def accept_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self)

    def reach_destination(self, ride):
        ride.end_ride()