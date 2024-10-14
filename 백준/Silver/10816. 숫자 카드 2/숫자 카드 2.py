def search_left(cards, target, l, r):
    while l < r:
        mid = (l + r) // 2
        if cards[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l

def search_right(cards, target, l, r):
    while l < r:
        mid = (l + r) // 2
        if cards[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return r

N = int(input())
cards = list(map(int,input().split()))
cards.sort()

M = int(input())
targets = list(map(int,input().split()))
ans = [0]*M

for i, target in enumerate(targets):
    left = search_left(cards, target, 0, N)
    right = search_right(cards, target, 0, N)
    if left <= right:
        ans[i] = right - left
print(*ans)
