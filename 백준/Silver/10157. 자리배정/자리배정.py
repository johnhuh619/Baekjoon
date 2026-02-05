

# up -> right -> down -> left
# % 4 = 0, 1, 2, 3
dx = [-1,0,1,0]
dy = [0,1,0,-1]

c, r = map(int,input().split())
k = int(input())
board = [[0]*c for _ in range(r)]

def spin(x, y):
    if  k > r*c:
        print(0)
        return
    
    cnt = 1
    d = 0
    board[x][y] = cnt
    while cnt < k:
        
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 0:
            x, y = nx, ny
            cnt += 1
            board[nx][ny] = cnt
            
        else:
            d = (d + 1) % 4
            
    print(y+1, r-x)
    return

spin(r-1,0)