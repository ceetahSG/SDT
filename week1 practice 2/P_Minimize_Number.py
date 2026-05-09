n = int(input())
nums = list(map(int, input().split()))
count = 0
while all (num % 2 == 0 for num in nums):
    nums = list(map(lambda x:x//2,nums))
    count+=1
print(count)

