class Ram:
    def __init__(self,size):
        self.size = size

class Cpu:
    def __init__(self,cores):
        self.cores = cores

class HardDisk:
    def __init__(self,capacity):
        self.capacityk = capacity
#computer has a ram
#computer has a processor
# computer has a harddisk --> has a relation
class Computer:
    def __init__(self,size,cores,capacity):
        self.size = size
        self.cores = cores
        self.capacity = capacity

mac = Computer(16,16000,100000)
