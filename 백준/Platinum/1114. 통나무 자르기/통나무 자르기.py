L, K, C = map(int, input().split())
points = list(map(int, input().split()))
points.sort()
points = [x for x in points if 0 < x < L]
points = [0, *points, L]
pieces = [points[i+1] - points[i] for i in range(len(points)-1)]
longest = max(pieces)

def cut(max_len):
    if longest > max_len:
        return C+1, 0
    sum = 0
    cnt = 0
    for p in pieces[::-1]:
        sum += p
        if sum > max_len:
            sum = p
            cnt += 1
    return cnt, sum if cnt == C else pieces[0]
            
    
l, r = 0, L
ans, ans_front = 0, 0
while l <= r:
    mid = (l+r)//2
    cnt, front = cut(mid)
    if cnt <= C:
        r = mid - 1
        ans = mid
        ans_front = front
    else:
        l = mid + 1
print(ans, ans_front)