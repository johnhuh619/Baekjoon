import sys
from collections import deque
n, m = map(int,input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
maxVal = 0
visited = [[False]*m for _ in range(n)]
def dfs(x,y, depth, current_sum):
    global maxVal
    if depth == 4:
        maxVal = max(maxVal, current_sum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+ 1, current_sum + graph[nx][ny])
            visited[nx][ny] = False
            
def check_exception(x,y):
    global maxVal
    for i in range(4):
        temp = graph[x][y]
        for j in range(3):
            k = (i+j) % 4
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0<= ny < m:
                temp += graph[nx][ny]
            else:
                break
        maxVal = max(maxVal,temp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
        check_exception(i,j)
print(maxVal)
