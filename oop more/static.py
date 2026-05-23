class Shopping:
    cart = [] #class attrubutes/ static attributes
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.cart = [] #instance attributes
    @classmethod
    def addToCart(self,item,price):
        print(f'{item} added to cart and price is {price}')
       
    
    @staticmethod
    def mul (a,b):
        result = a*b
        print(result)
    
jamuna = Shopping('jamuna','basundhara')
jamuna.addToCart('Phone',10000) #class method
Shopping.mul(50,2) #static method
