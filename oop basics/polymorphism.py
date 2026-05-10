class Animal:
    def __init__(self,name):
        self.name = name
    
    def make_sound(self) -> None:
        print('Making some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('Meow Meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print('Gheu Gheu')

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('meee meee')

tommy = Dog('Tom')

minu = Cat('Minu')

messi = Goat('Lionel')

tommy.make_sound()

minu.make_sound()

messi.make_sound()