import sys
from collections import deque
n,m = map(int,input().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
dir = [(1,0),(0,-1),(-1,0),(0,1)]
def bfs(start):
    ans = 0
    q = deque()
    i,j = start
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    q.append(start)
    while q:
        x, y = q.popleft()
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == 'O':
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                    if graph[nx][ny] == 'P':
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                        ans+=1
                    if graph[nx][ny] == 'X':
                        continue
    return ans
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            a = bfs((i,j))
            print(a if a != 0 else 'TT')
            break
