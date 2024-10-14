from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
    
def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 빙산이라면 큐에 추가
                if sea_origin[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

                # 빙산이 아니라면 바닷물로 카운트
                else:
                    cnt[x][y] += 1
    return 1    

N, M = map(int, input().split())
sea_origin = []                         # 초기 지도값 저장용
for _ in range(N):
    sea_origin.append(list(map(int,input().split())))
year = 0

while True:
    answer = []
    visited = [[0]*M for _ in range(N)]  # 방문 체크용
    cnt = [[0]*M for _ in range(N)]         # melt/year 기록용

    for i in range(N):
        for j in range(M):
            if sea_origin[i][j] != 0 and not visited[i][j]:
                answer.append(bfs(i,j))

    # 빙산 녹이기
    for i in range(N):
        for j in range(M):
            sea_origin[i][j] -= cnt[i][j]
            if sea_origin[i][j] < 0:
                sea_origin[i][j] = 0

    if len(answer) == 0 or len(answer) >= 2:
        break
    year += 1

print(year) if len(answer) >= 2 else print(0)