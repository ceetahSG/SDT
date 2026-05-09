n, q = map(int, input().split())
nums = list(map(int,input().split()))
prefix = [0]
for num in nums:
    prefix.append(prefix[-1]+num)
for i in range (q):
    l, r = map(int, input().split())
    ans = prefix[r] - prefix[l-1]
    print(ans)