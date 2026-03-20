from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())  # 가로, 세로
board = [list(map(int, input().strip())) for _ in range(n)]

INF = int(1e9)
dist = [[INF] * m for _ in range(n)]
dist[0][0] = 0

dq = deque()
dq.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            cost = dist[x][y] + board[nx][ny]

            if cost < dist[nx][ny]:
                dist[nx][ny] = cost

                if board[nx][ny] == 0:
                    dq.appendleft((nx, ny))
                else:
                    dq.append((nx, ny))

print(dist[n - 1][m - 1])