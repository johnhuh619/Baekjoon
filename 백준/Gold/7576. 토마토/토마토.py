from collections import deque
import sys


n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
visited= [[False]*(n) for _ in range(m)]
q = deque()
def bfs():
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]

  while q:
    x, y = q.popleft()

    for i in range(4) :
      nx, ny = dx[i]+x, dy[i]+y
      if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0 and visited[nx][ny] == False:
        graph[nx][ny] = graph[x][y] + 1
        visited[nx][ny] = True
        q.append((nx,ny))

# 탐색 시작할 첫 1 찾기
for x in range(m):
  for y in range(n):
    if graph[x][y] == 1:
      q.append((x,y))
      visited[x][y] = True
    
bfs()
ans = 0
flag = 0

for a in graph:
    for b in a:
        if b == 0:
            flag = 1
            break
    if flag == 1:
       break
    ans = max(ans, max(a))
if flag == 1:
   print(-1)
else:
   print(ans -1)