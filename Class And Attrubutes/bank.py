class Bank:
    type = 'saving'
    def __init__(self,balance):
        self.balance = balance
        self.minimum_withdraw = 500
        self.maximum_withdraw = 100000
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    def get_balance(self):
        print(self.balance)
    def withdraw(self,amount):
        if amount < self.minimum_withdraw:
            print(f'Minimum witdraw amount is {self.minimum_withdraw}')
        elif amount > self.maximum_withdraw:
            print(f'Sorry! You can\'t witdraw more than {self.maximum_withdraw}')
        else:
            self.balance -=amount
            print(f'New balance is {self.balance}')
brac = Bank(12500)
brac.get_balance()
brac.deposit(1000)
brac.get_balance()
brac.withdraw(100)
brac.withdraw(500)   