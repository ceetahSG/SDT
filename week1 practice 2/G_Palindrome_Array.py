n = input()
numbers = list(map(int,input().split()))
numbers2 = numbers[::-1]
if numbers == numbers2:
    print("YES")
else:
    print("NO")