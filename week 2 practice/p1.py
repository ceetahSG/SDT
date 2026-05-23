class Product:
    def __init__(self,product_name,id,price):
        self.name = product_name
        self.id = id
        self.price = price

class Shop:
    items = []
    def __init__(self,name,location):
        self.name = name
        self.location = location
        

    def add_product(self,product_name,id,price):
        item = Product(product_name,id,price)
        self.items.append(item)

    def buy_product(self,name):
        for item in self.items:
            if item.name == name:
                print('Item available')
                print('Congrats, you have sucessfully bought the product')
            else:
                print('Sorry item not available')

unimart = Shop('Unimart','Dhanmondi')
unimart.add_product('Clear man shampoo','p1',1000)

unimart.buy_product('Clear man shampoo')
unimart.buy_product('toy')

