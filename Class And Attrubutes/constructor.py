class Phone:
    manufacture = 'china'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price
    def send_sms(self,phone,sms):
        text = f'sending to:{phone} {sms}'
        print(text)
myPhone = Phone('Sajim','I phone',60000)
herPhone = Phone('Her','Oppo',20000)

print(myPhone.brand,myPhone.owner,myPhone.price)
myPhone.send_sms(123123,"hlw how are you?")

        