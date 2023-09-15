from collections import deque
import sys
# 6방위 전, 후, 좌, 우, 상, 하
# 2/1 (3) 가지 상태. ( (0, 1), -1 ) 

m, n, h = map(int,sys.stdin.readline().split())
graph = [[list(map(int,sys.stdin.readline().split()))for _ in range(n)] for _ in range(h) ]
visited = [[[False]*(m) for _ in range(n)] for _ in range(h)]

q = deque()

def bfs(x,y,z):

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1 ,-1]

    while q:
        x,y,z = q.popleft()
        
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                # bfs를 반복해서 돌리기 ㄴㄴ +=1 해버리면 일수 측정 가능
                # 현재 위치가 익었을때
                # 1-1. 이동 위치가 안익었으면 익음 처리
                # 1-2. 익은 좌표의 값을 이전 토마토 값 += 1
                # 1-3. 이것을 통해 익은 토마토의 단계(날짜)를 알 수 있다.
                if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                    q.append((nx,ny,nz))
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    visited[nx][ny][nz] = True
# 첫번째 1을 찾기
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i,j,k))
                visited[i][j][k] = True

bfs(0,0,0)

ans = 0
flag = 0
for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                flag = 1
                break
        ans = max(ans,max(b))

if flag == 1:
    print(-1)
else:
    print(ans-1)