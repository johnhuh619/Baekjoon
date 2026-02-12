n, m = map(int, input().split())
gate = [int(input()) for _ in range(n)]

# a  b
# 7 10

l = 0
r = max(gate)*m
ans = r

while l <= r:
    mid = (l+r) // 2
    tot = 0
    for t in gate:
        tot += mid // t
    
    if tot >= m:
        ans = mid
        r = mid - 1
    
    else:
        l = mid + 1
print(ans)
        
