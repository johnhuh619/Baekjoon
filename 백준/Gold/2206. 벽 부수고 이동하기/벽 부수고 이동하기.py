from collections import deque
import sys
n, m = map(int,input().split())

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,z): 
  #기본값 n = 0
    visited[x][y][z] = 1
    q = deque()
    q.append((x,y,z))
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        # 상하좌우 무브 무브~
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
        # 다음 이동이 벽 & 0회차 
            if graph[nx][ny] == 1 and z == 0 :
                # 필드 변경 
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx,ny,1))
            #다음 이동이 !벽 & 방문 x
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx,ny,z))
    return -1 

print(bfs(0,0,0))