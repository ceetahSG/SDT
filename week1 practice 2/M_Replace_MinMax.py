n = int(input())
arr = list(map(int,input().split()))

min_ind = arr.index(min(arr))
max_ind = arr.index(max(arr))

arr[min_ind],arr[max_ind] = arr[max_ind],arr[min_ind]
print(*arr)
    
