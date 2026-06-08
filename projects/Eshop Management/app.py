from user import Customer,Seller
from order import Order
class EshopingApp:
    def __init__(self):
        self.customers = {}
        self.sellers = {}
        self.products = []
        self.orders = []
    
    def register_customer(self,email,password):
        if email not in self.customers:
            self.customers[email]= Customer(email,password)
            print(f"System: Customer account created for {email}")
            return self.customers[email]
        print("System: Email already registered")
        return None
    
    def register_seller(self,email,password):
        if email not in self.sellers:
            self.sellers[email]= Seller(email,password)
            print(f"System: Seller account created for {email}")
            return self.sellers[email]
        print("System: Email already registered")
        return None
    
    def add_product(self,product):
        self.products.append(product)
    
    def view_available_products(self):
        print("\n---Available Products---")
        available_products = [p for p in self.products if p.is_in_stock()]
        if not available_products:
            print("No products currently available.")
        else:
            for p in available_products:
                print(f"-{p.name} | Price: {p.price} | Stock: {p.stock} | Sold by: {p.seller.email}---------\n")
    
    def process_order(self,customer,product_name,quantity):
        for product in self.products:
            if product.name == product_name:
                if product.stock >= quantity:
                    product.stock -= quantity
                    order = Order(customer,product,quantity)
                    self.orders.append(order)
                    customer.orders.append(order)

                    print(f"Success: {customer.email} bought {quantity}x {product.name} for ${order.total_price}.")
                    return True
                else:
                    print(f"Failed: Not enough stock for '{product.name}'. Only {product.stock} left.")
                    return False
        print(f"Failed: Product '{product_name}' not found.")
        return False

    
    
    
        
        