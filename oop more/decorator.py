import math
def func(fnc):
   
    def innerFunc(*args,**kwargs):
        print('Func started')
        fnc(*args,**kwargs)
        print('Func ended')
    return innerFunc

@func
def factorial(n):
    print('Factorial started')
    res = math.factorial(n)
    print(f'Factorial of {n} is {res}')

factorial(5)