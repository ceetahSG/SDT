from menu import Menu
class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} is added successfully!!')

    def view_employee(self):
        for emp in self.employees:
            print(emp.name, emp.age, emp.phone)