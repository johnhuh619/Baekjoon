from collections import deque
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(sx, sy, visited):
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = True
    
    union = [(sx, sy)]
    hnum = board[sx][sy]
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(board[x][y] - board[nx][ny]) <= R:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    union.append((nx,ny))
                    hnum += board[nx][ny]

    return union, hnum

days = 0
while True:
    visited = [[False]*N for _ in range(N)]
    
    moved = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, hnum = bfs(i,j,visited)
                if len(union) > 1:
                    moved = True
                    avg = hnum // len(union)
                    for x, y in union:
                        board[x][y] = avg
    if not moved:
        break
    
    days += 1
    
print(days)
                    
