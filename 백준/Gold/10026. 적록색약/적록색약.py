from collections import deque
n = int(input())
graph = [list(input().strip()) for _ in range(n)]

NORMAL = 0
ABNORMAL = 1

visited = [
    [[False]*n for _ in range(n)],
    [[False]*n for _ in range(n)]
]

dir = [(1,0), (-1,0), (0,1), (0,-1)]

def is_same_color(a, b, mode):
    if mode == NORMAL:
        return a == b
    if a == 'B' or b == 'B':
        return a == b
    return True

def bfs(r,c, mode):
    q = deque([(r,c)])
    visited[mode][r][c] = True
    color = graph[r][c]
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy 
            if 0 <= nx <n and 0 <= ny < n and not visited[mode][nx][ny]:
                if is_same_color(color, graph[nx][ny], mode):    
                    visited[mode][nx][ny] = True
                    q.append((nx,ny))

cnt = [0,0]
for m in [NORMAL,ABNORMAL]:
    for i in range(n):
        for j in range(n):
            if not visited[m][i][j]:
                bfs(i,j,m)
                cnt[m] += 1
print(cnt[0], cnt[1])

