from datetime import datetime
from vehicle import Car,Bike
class RideSharing:
    def __init__(self,company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.drivers.append(driver)
    def __str__(self):
        return f"Company Name: {self.company_name} with riders:{len(self.riders)} and Drivers: {len(self.drivers)}"

class Ride:
    def __init__(self,start_location,end_location,vehicle):
        self.start_location = start_location
        self.vehicle = vehicle
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self,driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    def __repr__(self):
        return f"Ride details.Started {self.start_location} to {self.end_location}"

def calculate_fare(distance, vehicle_type):
    fare_per_km = {
        'car': 30,
        'bike': 20,
        'cng': 25
    }
    return distance * fare_per_km.get(vehicle_type, 0)

class RideRequest:
    def __init__(self,rider,end_location):
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self,drivers):
        self.available_drivers = drivers
    
    def find_driver(self,ride_request,vehicle_type):
        if len(self.available_drivers) >0:
            print("Looking for drivers.................")
            driver = self.available_drivers.pop(0)
            if vehicle_type == 'car':
                vehicle = Car('car', "A1495VB", 150)
            elif vehicle_type == 'bike':
                vehicle = Bike('bike', "MB2582", 100)
            else:
                # fallback vehicle
                vehicle = Car('car', "A1495VB", 150)

            ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)
            # attach rider and a simple estimated fare so end_ride can process payments
            ride.rider = ride_request.rider
            # simple flat distance assumption for demo purposes
            ride.estimated_fare = vehicle.rate * 5

            driver.accept_ride(ride)
            return ride
