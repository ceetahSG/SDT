person = {'name':'rahim', 'age': 30, 'city': 'dhaka'}

print(person.keys())
print(person.values())
person['country'] = 'bangladesh'
print(person)
person['name'] = 'karim'
del person['age']
print(person)

for key,value in person.items():
    print(key, value)