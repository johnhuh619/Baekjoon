from collections import deque


# RGB 로 cnt 하고 2. 로 GGB 로 cnt
def bfs(x,y):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if graph[nx][ny] == graph[x][y]:
                        visited[nx][ny] = 1
                        q.append((nx,ny))
def change(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'R':
                graph[i][j] = 'G'

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1

change(graph)
visited = [[0]*n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2+=1

print(cnt, cnt2)