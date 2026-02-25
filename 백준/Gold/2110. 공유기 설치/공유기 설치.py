n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

def install(mid):
    cnt = 1
    last = houses[0]
    for i in range(1, n):
        if houses[i] - last >= mid:
            cnt += 1
            last = houses[i]
    return cnt
l, r= 1, houses[-1] - houses[0]
ans = 0

while l <= r:
    mid = (l+r) // 2
    cnt = install(mid)

    if cnt >= c:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
            