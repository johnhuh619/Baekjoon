N = int(input())
arr = list(map(int, input().split()))
p,q,r,s = map(int,input().split())

low, high = 1, 2*10**10

while low <= high:
    tot = 0
    mid = (low+high) // 2
    for n in arr:
        if n > mid + r:
            tot += n - p
        elif n < mid:
            tot += n + q
        else:
            tot += n
    if tot >= s:    
        high = mid - 1
    
    else:
        low = mid + 1

if high == 2*10**10:
    print(-1)
else:
    print(low)



