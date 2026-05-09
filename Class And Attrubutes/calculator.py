class Calculator:
    brand = 'Casio'
    def add(self,num1,num2):
        return num1+num2
    def subtract(self,num1,num2):
        return num1 - num2
    def multiply(self,num1,num2):
        return num1*num2
    def divide (self,num1,num2):
        return num1//num2

calculator = Calculator()
res = calculator.divide(12,12)
print(res)