from collections import deque

def tomato(graph):
    queue = deque()

    # 익은 토마토와 큐 초기화
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))
                    visited[i][j][k] = True

    # BFS 수행
    dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
    day = 0
    while queue:
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= nx < h and 0 <= ny < m and 0 <= nz < n and not visited[nx][ny][nz] and graph[nx][ny][nz] == 0:
                    queue.append((nx, ny, nz))
                    visited[nx][ny][nz] = True
                    graph[nx][ny][nz] = 1
        day += 1

    # 모든 토마토가 익었는지 확인
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if graph[i][j][k] == 0:
                    return -1
    return day - 1 if day > 0 else 0

# 입력 받기
n, m, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
visited = [[[False] * n for _ in range(m)] for _ in range(h)]
print(tomato(graph))
