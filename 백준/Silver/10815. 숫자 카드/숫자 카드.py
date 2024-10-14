N = input()
cards = list(map(int,input().split()))
cards.sort()

M = int(input())
targets = list(map(int,input().split()))
ans = [0]*M
i = 0
for target in targets:
    l, r = 0, len(cards) -1
    while l <= r:
        mid = (l+r)//2
        check = cards[mid]
        if check == target:
           ans[i] = 1
           break
        elif target < check:
            r = mid - 1
        elif target > check:
            l = mid + 1
    i += 1
print(*ans)
