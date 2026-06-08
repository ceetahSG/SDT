from product import Product


class User:
    def __init__(self,email,password):
        self.email = email
        self.__password = password
    
    def verify_password(self,password):
        return self.__password == password
    
class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.orders = []
    
    def place_order(self,app,product_name,quantity):
        return app.process_order(self,product_name,quantity)

class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
    
    def publish_product(self,app,name,price,stock):
        product = Product(name,price,stock,self)
        app.add_product(product)
        print(f"[Seller: {self.email}] Published: {name} (Stock: {stock})")