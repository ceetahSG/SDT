numbers = [23, 45, 67, 89, 23, 45]
unique_numbers = set(numbers)
print(unique_numbers)
unique_numbers.add(100)
print(unique_numbers)
for num in unique_numbers:
    print(num)
if 45 in unique_numbers:
    print('45 is present') 
else:    
    print('45 is not present') 

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B ) #union
print(A & B) #intersection
print(A - B) #difference