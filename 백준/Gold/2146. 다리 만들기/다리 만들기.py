import sys
from collections import deque



dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs1(i,j):
    global inum
    q = deque()
    q.append((i,j))
    visit[i][j] = True
    graph[i][j] = inum

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <n and 0<= ny <n and graph[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                graph[nx][ny] = inum
                q.append((nx,ny))


def bfs2(z):
    global ans
    distance = [[-1]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == z:
                q.append((i,j))
                distance[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if graph[nx][ny] > 0 and graph[nx][ny] != z:
                ans = min(ans, distance[x][y])
                return
            if graph[nx][ny] == 0 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))                


n = int(input())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
inum = 1
ans = sys.maxsize
for i in range(n):
    for j in range(n):
        if not visit[i][j] and graph[i][j] == 1:
            bfs1(i,j)
            inum += 1

for i in range(1, inum):
    bfs2(i)
print(ans)
