n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


# i,j => 

depth = min(n, m) // 2
for d in range(depth):
    temp = []

    top, left = d, d
    bot, right = n - d - 1, m - d - 1
    
    # up -> down
    for i in range(top, bot):
        temp.append(board[i][left])
    
    # left -> right
    for j in range(left, right):
        temp.append(board[bot][j])
    
    # down -> up
    for i in range(bot, top, -1):
        temp.append(board[i][right])
    
    # right -> left
    for j in range(right, left, -1):
        temp.append(board[top][j])
    
    sp = r % len(temp)
    temp = temp[-sp:] + temp[:-sp]
    
    idx = 0
    # replace
    for i in range(top, bot):
        board[i][left] = temp[idx]
        idx += 1
    
    for j in range(left, right):
        board[bot][j] = temp[idx]
        idx += 1
    
    for i in range(bot, top, -1):
        board[i][right] = temp[idx]
        idx += 1
    
    for j in range(right, left, -1):
        board[top][j] = temp[idx]
        idx += 1
    
for row in board:
    print(*row)