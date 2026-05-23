def doubleDecker():
    print('inside double decker')
    def inner():
        print('Inside innner func')
        return 3000
    return inner
    

print(doubleDecker()())

def doSomething(work):
    print('work started')
    work()
    print('work ended')

def coding():
    print('Coding in python')

doSomething(coding)