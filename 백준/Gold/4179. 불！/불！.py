from collections import deque
r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

vistied_fire = [[0] * (c) for _ in range(r)]
visited_j = [[0] * (c) for _ in range(r)]

def bfs_fire(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != "#" and vistied_fire[nx][ny] == 0:
                    # time
                    vistied_fire[nx][ny] = vistied_fire[x][y] + 1
                    q.append((nx,ny))

def bfs_j(x, y):
    q = deque([(x,y)])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return visited_j[x][y] + 1
            
            if vistied_fire[nx][ny] != 0 and vistied_fire[nx][ny] <= visited_j[x][y] + 1:
                continue
            
            if board[nx][ny] == '.' and visited_j[nx][ny] == 0:
                visited_j[nx][ny] = visited_j[x][y] + 1
                q.append((nx, ny))

    return None

fires = deque()
x, y = 0, 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            x, y = i, j
        if board[i][j] == 'F':
            fires.append((i,j))
bfs_fire(fires)
res = bfs_j(x, y)
if res:
    print(res)
else:
    print("IMPOSSIBLE")
                
                