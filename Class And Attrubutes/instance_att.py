class Shop:
    mall = 'Jamuna'
    def __init__(self,name):
        self.name = name
        self.cart = []
    def add_to_cart(self,item):
        self.cart.append(item)
rahim = Shop('Rahim')
karim = Shop('Karim')
rahim.add_to_cart('shoe')
rahim.add_to_cart('watch')
rahim.add_to_cart('belt')
rahim.add_to_cart('phone')
print(rahim.cart)

karim.add_to_cart('ice cream')
karim.add_to_cart('biscuit')
karim.add_to_cart('chanachur')
karim.add_to_cart('coca cola')
print(karim.cart)

