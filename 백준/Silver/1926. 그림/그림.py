from collections import deque
from itertools import count
import pickle

n,m = map(int,input().split())
# n x m 방문 유무 확인해주는 리스트
visited = [[False]*m for _ in range(n)]    
# 주어진 그래프 리스트로 표현
graph = [list(map(int,input().split())) for _ in range(n)]
# 격자 탐색을 위한 기본 로직
dx = [1, -1, 0, 0] # 좌우 -1, 1
dy = [0, 0, 1, -1] # 상하 -1, 1

each = 0
result = []
def bfs (x,y):
    cnt = 1

    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] == 1 :
                    cnt += 1
                    q.append([nx,ny])
                    visited[nx][ny] = True
    return cnt

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1 and visited[x][y] == False:
            visited[x][y] = True
            pic = bfs(x,y)
            result.append(pic)

if len(result) == 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))
