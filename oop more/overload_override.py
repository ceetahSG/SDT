class Person:
    def __init__(self,name,age,weight,heigh):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = heigh
    
    def eat(self):
        print('vat,mangsho,polau,korma')
    
    def exercie(self):
        raise NotImplemented

class Cricket(Person):
    def __init__(self, name, age, weight, heigh,team):
        super().__init__(name, age, weight, heigh)
        self.team = team
    def eat(self): #override
        print('vagetables,bun')
    def exercie(self):
        print('tk diye gym kori mama')
    
    def __add__(self, other): #overloading +
        return self.age + other.age
    
    

sakib = Cricket('sakib',36,75,67,'BD')
Tamim = Cricket('Tamim',46,72,90,'BD')
sakib.eat()
sakib.exercie()
print(sakib+Tamim)



