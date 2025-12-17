from collections import deque
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    dir = [
        (1,0),
        (0,1),
        (-1,0),
        (0,-1)
    ]
    q = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append((i,j))
    
    while q:
        x, y = q.popleft()    
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))
bfs()
ans = 0
for row in box:
    if 0 in row:
        print(-1)
        exit()
    ans = max(ans, max(row))
if ans == 1:
    print(0)
else:
    print(ans-1)