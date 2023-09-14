from collections import deque
import sys
n = int(input())
graph = []
ans = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

def bfs(x,y):
    q = deque()
    q.append((x,y))

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 1
    graph[x][y] += 1
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append((nx,ny))
                cnt += 1
                graph[nx][ny] += 1  
    ans.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
ans.sort()
print(len(ans))
for i in ans:
    print(i)