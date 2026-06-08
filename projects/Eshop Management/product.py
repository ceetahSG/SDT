class Product:
    def __init__(self,name,price,stock,seller):
        self.name = name
        self.price = price
        self.stock = stock
        self.seller = seller
    
    def is_in_stock(self):
        return self.stock >0
    