h, w = map(int, input().split())
board = list(map(int, input().split()))

left = [0]*w
right = [0]*w

left[0] = board[0]
for i in range(1, w):
    left[i] = max(left[i-1], board[i])

right[-1] = board[-1]
for i in range(w-2, -1, -1):
    right[i] = max(right[i+1], board[i])

ans = 0
for i in range(w):
    ans += min(left[i], right[i]) - board[i]

print(ans)    