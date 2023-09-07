from collections import deque
import sys
i = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,graph):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
    return



for i in range(i):
    n, m, s = map(int,input().split())
    graph = [[0]*(m) for _ in range(n)]
    cnt = 0

    for _ in range(s):
        x,y = map(int,input().split())
        graph[x][y] = 1

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                bfs(x,y,graph)
                cnt+=1
    print(cnt)