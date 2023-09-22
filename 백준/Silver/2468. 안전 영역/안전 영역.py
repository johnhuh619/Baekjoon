from collections import deque
import sys

n = int(input())
graph = []
max_height = 0
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    max_height = max(max_height,max(graph[i]))
                 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()

def bfs(x,y,t):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if  graph[nx][ny] > t:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

result = 0
for i in range(max_height):
    visited = [[0]*(n) for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i)
                count += 1
    result = max(result,count)
print(result)

        

