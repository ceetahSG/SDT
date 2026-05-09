add  = lambda x,y : x+y
square = lambda x : x*x
print(add(6,5))

nums = [34,65,23,51,52,67]
double_nums = map(lambda x : x*x ,nums)
print(nums)
print(list(double_nums))

actors = [
    {'name':'sabana','age':35},
    {'name':'shakib','age':42},
    {'name':'rahim','age':15},
    {'name':'shaon','age':25},
]
juniors = filter(lambda actor:actor['age']<30,actors)
fivers = filter(lambda x:x['age']%5 == 0,actors)
print(list(fivers))
# print(list(juniors))