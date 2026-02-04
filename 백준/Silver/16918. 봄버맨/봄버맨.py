r, c, n = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

field = [[3 if board[i][j] == "O" else 0 for j in range(c)] for i in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for t in range(1, n+1):
    boom = []
    for i in range(r):
        for j in range(c):
            if field[i][j] > 0:
                field[i][j] -= 1
                
                if field[i][j] == 0:
                    boom.append((i,j))
                    
    if t % 2 == 0:
        for i in range(r):
            for j in range(c):
                if field[i][j] == 0:
                    field[i][j] = 3
                    
    else:
        for x, y in boom:
            field[x][y] = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    field[nx][ny] = 0
                    
for i in range(r):
    print(''.join('O' if field[i][j] > 0 else '.' for j in range(c)))