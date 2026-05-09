from collections import Counter
n = int(input())
a = list(map(int,input().split()))

freq = Counter(a)
res = 0
for digit in a:
    if(freq[digit]>=digit):
        res += freq[digit] - digit
        freq[digit] = digit
    else:
        res += freq[digit]
        freq[digit] = 0
print(res)



