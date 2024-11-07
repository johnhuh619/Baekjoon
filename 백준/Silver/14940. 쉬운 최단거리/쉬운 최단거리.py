import sys
from collections import deque
n, m = map(int,input().split())
res = []
for _ in range(n):
    res.append(list(map(int, sys.stdin.readline().split())))

visited = [[-1]*m for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(rs,cs):
    q = deque()
    visited[rs][cs] = 0
    q.append((rs,cs))
    while q:
        x, y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if visited[nx][ny] == -1 and res[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if res[i][j] == 2:
            rs, cs = i, j
        if res[i][j] == 0:
            visited[i][j] = 0
bfs(rs,cs)
for i in range(n):
    print(*visited[i])
    