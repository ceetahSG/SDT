class Bank:
    def __init__(self,holder_name,balance,id):
        self.holder_name = holder_name
        self.__balance = balance
        self._id = id
    def get_balance(self):
        return f'Balance:{self.__balance}'
    
    def account_num(self):
        return f'Account Number:{self._id}'
    
    
Rahim = Bank('Rahim',10000,23560)
print(Rahim.holder_name)
print(Rahim.get_balance())
print(Rahim.account_num())