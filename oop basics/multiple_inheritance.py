class Family:
    def __init__(self,address,cast):
        self.address = address
        self.cast = cast
    
class School:
    def __init__(self,level,id):
        self.level = level
        self.id = id

class Club:
    def __init__(self,games):
        self.games = games

class Student(Family,School,Club):
    def __init__(self, address, cast,level,id,games):
        Family.__init__(self,address,cast)
        School.__init__(self,level,id)
        Club.__init__(self,games)
    def __repr__(self):
        return f'{self.address},{self.cast},{self.level},{self.id},{self.games}'
        
    
Rahim = Student('Dhanmondi','Brahman',10,101,'Football')
print(Rahim)
        