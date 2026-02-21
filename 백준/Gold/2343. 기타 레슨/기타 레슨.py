n, m = map(int, input().split())
times = list(map(int, input().split()))

l, r = max(times), sum(times)
ans = 0
while l <= r:
    mid = (l+r) // 2
    tot = 0
    cnt = 1
    for t in times:
        if tot + t > mid:
            cnt += 1
            tot = 0
        tot += t
    if cnt <= m:
        ans = mid
        r = mid -1
    else:
        l = mid + 1
        
print(ans)