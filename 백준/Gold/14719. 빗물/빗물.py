h, w = map(int, input().split())
board = list(map(int, input().split()))

l, r = 0, w-1
lmax, rmax = board[l], board[r]
ans = 0

while l < r:
    if lmax <= rmax:
        l += 1
        lmax = max(lmax, board[l])
        ans += lmax - board[l]
    else:
        r -= 1
        rmax = max(rmax, board[r])
        ans += rmax - board[r]
        
print(ans)    