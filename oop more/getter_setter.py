class User:
    def __init__(self,name,age,money):
        self.name = name
        self._age = age
        self.__money = money
    
    @property #getter
    def salary(self):
        return self.__money
    
    @salary.setter #setter
    def salary(self,value):
        if value < 0:
            return 'Value cant\'t be negative'
        self.__money +=value

rahim = User('Rahim',25,10000)
print(rahim.salary)
rahim.salary = 1000
print(rahim.salary)