s = input()
countL = 0
countR = 0
current = ""
result = []

for char in s:
    current +=char

    if char == 'L':
        countL +=1
    else:
        countR +=1
    if countL == countR:
        result.append(current)
        current = ""
print(len(result))
for item in result:
    print(item)