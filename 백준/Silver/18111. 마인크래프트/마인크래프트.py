n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')

# add / remove
floor = 0
for cur in range(257):
    add, rem = 0, 0
    
    for i in range(n):
        for j in range(m):
            # 2초
            if board[i][j] >= cur:
                rem += board[i][j] - cur
            # 1초
            else:
                add += cur - board[i][j]
    
    if add > rem + b:
        continue
    
    t = rem*2 + add 
    if t < ans or (t == ans and cur > floor):
        ans = t
        floor = cur

print(ans, floor)
        

                