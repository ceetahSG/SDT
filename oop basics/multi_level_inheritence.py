class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'Name:{self.name}, Price:{self.price}'

class Bus(Vehicle):
    def __init__(self, name, price,seat):
        self.seat = seat
        super().__init__(name, price)
    
    def __repr__(self):
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price,max_weight):
        self.max_weight = max_weight
        super().__init__(name, price)
    
    def __repr__(self):
        return super().__repr__()

class MiniTruck(Truck):
    def __init__(self, name, price, max_weight,cage):
        self.cage = cage
        super().__init__(name, price, max_weight)
    def __repr__(self):
        return super().__repr__()

class ACBus(Bus):
    def __init__(self, name, price, seat,fare):
        self.fare = fare
        super().__init__(name, price, seat)
    def __repr__(self):
        print(f'Seat: {self.seat},Fare: {self.fare}')
        return super().__repr__()


green_line = ACBus('Green Line',50000000,40,1600)
print(green_line)