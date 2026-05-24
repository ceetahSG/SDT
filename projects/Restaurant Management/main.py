from users import Admin,Customer,Employee
from restaurant import Restaurent
from item import Item
from menu import Menu
from order import Order

R = Restaurent("Mayer Doa")
def customer_menu():
    name = input("Enter you name:")
    email = input("Enter your email:")
    address = input("Enter your address:")
    phone = input("Enter your phone number:")

    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1.View Menu")
        print("2.Order Item")
        print("3.View Order")
        print("4.Pay Bill")
        print("5.Exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            customer.view_menu(R)
        elif choice == 2:
            item_name = input("Enter item name:")
            quantity = int(input("Enter quantity:"))
            customer.add_to_cart(R,item_name,quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid choice!")
def admin_menu():
    name = input("Enter you name:")
    email = input("Enter your email:")
    address = input("Enter your address:")
    phone = input("Enter your phone number:")

    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {admin.name}")
        print("1.Add Item")
        print("2.Add Employee")
        print("3.View Items")
        print("4.View Employees")
        print("5.Remove Item")
        print("6.Exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            item_name = input("Enter item name:")
            item_price = int(input("Enter item price:"))
            item_quantity =int(input("Enter item quantity:"))
            item = Item(item_name,item_price,item_quantity)
            admin.add_item(R,item)
        elif choice == 2:
            name = input("Enter name:")
            email = input("Enter email:")
            phone = input("Enter phone num:")
            address = input("Enter address:")
            designation = input("Enter designation")
            salary = input("Enter salary:")
            age = input("Enter age:")
            employee = Employee(name,email,phone,address,designation,salary,age)
            admin.add_employee(R,employee)
        elif choice == 3:
            admin.view_menu(R)
        elif choice == 4:
            admin.view_employee(R)
        elif choice == 5:
            item = input("Enter item name:")
            admin.remove_item(R,item)
        elif choice == 6:
            break
        else:
            print("Invalid choice!")

print("Welcome to restaurent management system")
while True:
    print("1.Admin")
    print("2.Customer")
    print("3.Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Choice!!")




    