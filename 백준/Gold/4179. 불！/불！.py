from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited_fire = [[0 for _ in range(M)] for _ in range(N)]
visited_J = [[0 for _ in range(M)] for _ in range(N)]

pos_J = None
pos_fire = None

# Bfs -> queue
fire_q = deque()
J_q = deque()

for j in range(N):
    for i in range(M):
        if maze[j][i] == 'J':
            pos_J = (i, j)
            J_q.append(pos_J)
            visited_J[j][i] = 1
        elif maze[j][i] == 'F':
            pos_fire = (i, j)
            fire_q.append(pos_fire)
            visited_fire[j][i] = 1

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def fire_bfs():
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if maze[ny][nx] in ['.', 'J'] and visited_fire[ny][nx] == 0:
                    fire_q.append((nx, ny))
                    visited_fire[ny][nx] = visited_fire[y][x] + 1

fire_bfs()

def j_bfs():
    while J_q:
        x, y = J_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 탈출 조건
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                return visited_J[y][x]
            # 불이 이미 번진 경우
            if visited_fire[ny][nx] != 0 and visited_fire[ny][nx] <= visited_J[y][x] + 1:
                continue
            if maze[ny][nx] == '.' and visited_J[ny][nx] == 0:
                J_q.append((nx, ny))
                visited_J[ny][nx] = visited_J[y][x] + 1

result = j_bfs()

if result:
    print(result)
else:
    print("IMPOSSIBLE")