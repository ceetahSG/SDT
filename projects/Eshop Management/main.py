from user import Customer,Seller
from order import Order
from product import Product
from app import EshopingApp

daraz = EshopingApp()

rahim = daraz.register_customer("rahim@gmail.com","pass1234")
karim = daraz.register_seller("karim@gmail.com","pass2234")

# Use dot for decimal separator (999.00) or plain integers for price
karim.publish_product(daraz, "Laptop", 999.00, 2)
karim.publish_product(daraz, "Mouse", 120.00, 5)

daraz.view_available_products()

rahim.place_order(daraz,"Mouse",1)
rahim.place_order(daraz,"Laptop",1)

daraz.view_available_products()

rahim.place_order(daraz,"Laptop",3)