from abc import ABC

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Employee(User):
    def __init__(self, name, email, phone, address,designation,salary,age):
        super().__init__(name, email, phone, address)
        self.designation = designation
        self.salary = salary
        self.age = age
        
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.employees = []
        
    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)
    
    def view_employee(self,restaurent):
        restaurent.view_employee()
    
    def add_item(self,restaurent,item):
        restaurent.menue.add_item(item)
    def remove_item(self,restaurent,item):
        restaurent.menue.remove_item(item)
    def view_menue(self,restaurent):
        restaurent.menue.show_menue()

class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menue = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} is added successfully!!')

    def view_employee(self):
        for emp in self.employees:
            print(emp.name, emp.age, emp.phone)

class Menu:
    def __init__(self):
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)
    
    def find_item(self,item_name):
        for item in self.items:
            if item_name.lower() == item.name.lower():
                return item
            else:
                return None
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
        else:
            print("Item not found.")

    def show_menue(self):
        print("********Menue*********")
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

R1  = Restaurent('Mayer Doa')
admin = Admin('Sajim','sajim.ceetah@gmail.com',123141245,'Dhanmondi')
emp1 = Employee('Raj','raj@gmail.com','845392','Dhaka','Care taker',6000,20)
admin.add_employee(R1,emp1)
admin.view_employee(R1)

pizza = Item('Pizza',120.23,20)
admin.add_item(R1,pizza)
admin.view_menue(R1)
