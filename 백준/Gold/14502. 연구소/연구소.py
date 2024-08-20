from collections import deque
import copy
N,M = map(int, input().split())
base_graph = [list(map(int, input().split())) for _ in range(N)] 


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    graph = copy.deepcopy(base_graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx,ny))
    global ans
    cnt = 0

    for i in range(N):
        cnt += graph[i].count(0)
    ans = max(ans, cnt)
    
def makeWall(wall):
    if wall == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if base_graph[i][j] == 0:
                base_graph[i][j] = 1
                makeWall(wall+1)
                base_graph[i][j] = 0

ans = 0
makeWall(0)
print(ans)