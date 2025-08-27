N = int(input())
L = list(map(int, input().split()))
M = int(input())

l = 1
r = max(L)
ans = 0     
while l <= r:
    mid = (l+r) // 2
    tot = 0
    for lst in L:
        tot += min(lst, mid)
        
    if tot <= M:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
        
print(ans)
        
        