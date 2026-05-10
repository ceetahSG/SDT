from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        print('I eat something')
    
    @abstractmethod
    def move(self):
        print('I can move')

class Monkey(Animal):
    def __init__(self,name):
        self.name = name
        self.category = 'Monkey'
        super().__init__()
    def eat(self):
        print('I eat banana')
    def move(self):
        print('I cant move i only jump')

sher = Monkey('sher')
sher.eat()
sher.move()