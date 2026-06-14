from abc import ABC

class Vehicle(ABC):
    speed = {
        'car' :60,
        'bike' :70,
        'cng' :45
    }
    def __init__(self,vehicle_type,license_plate,rate):
        self.vehicle = vehicle_type
        self.license_plate = license_plate
        self.rate = rate

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)