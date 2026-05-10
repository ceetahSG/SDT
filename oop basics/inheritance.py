class Device:
    def __init__(self,brand,price,origin,color):
        self.brand = brand
        self.price = price
        self.origin = origin
        self.color = color
    def run(self):
        return f'This device is running and brand name is: {self.brand}'

class Laptop:
    def __init__(self,display,ram):
        self.display = display
        self.ram = ram
    def code(self):
        return f'This device is running python'

class Phone(Device):
    def __init__(self,brand,price,origin,color,dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand,price,origin,color)
    def call(self):
        return f'Calling to someone unknown'

    def __repr__(self)->str:
        return f'phone: {self.brand}, Color:{self.color},Origin:{self.origin},Dual Sim::{self.dual_sim}'

class Camera:
    def __init__(self,lens):
        self.lens = lens
    def change_lens(self):
        return f'lens is changed'
    
myphone = Phone('Iphone',12000,'Japan','Aqua',False)
print(myphone)

