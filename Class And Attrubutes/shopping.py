class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    def add_to_cart(self,name,price,quantity):
        items = {'name':name,'price':price,'quantity':quantity}
        self.cart.append(items)
    def remove_item(self,item_name):
        for item in self.cart:
            if(item['name'] == item_name):
                self.cart.remove(item)
                break
    
    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total += item['price']* item['quantity']
        if amount > total:
            print (f'Here is your items and exchange {amount - total}')
        else:
            print(f'Please provide {total - amount} more')
    
Rahim = Shopping("Rahim Uddin")
Rahim.add_to_cart('Poatoe',40,5)
Rahim.add_to_cart('Tomato',50,2)
Rahim.add_to_cart('Cucumber',70,2)
print(Rahim.cart)
Rahim.remove_item('Tomato')
print(Rahim.cart)

Rahim.checkout(1000)






        