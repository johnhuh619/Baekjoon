from itertools import combinations
from collections import deque
# 입력값 받기
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

def find_rumtime(N, M, lab):
    virus_location = [(u,v) for u in range(N) for v in range(N) if lab[u][v] == 2]
    min_time = float('inf')
    # [(a,b), (c,d), ...] 
    for active_virus in combinations(virus_location, M):
        time = bfs(lab, active_virus, N) 
        min_time = min(min_time, time)

    return min_time if min_time != float('inf') else -1

def bfs(lab, active_virus, N):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque(active_virus)
    visited = [[-1]*N for _ in range(N)]
    max_time = 0

    for r, c in active_virus:
        visited[r][c] = 0
    
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[r][c] + 1
                    queue.append((nx,ny))
                    if lab[nx][ny] == 0:
                        max_time = max(max_time, visited[nx][ny])

    for r in range(N):
        for c in range(N):
            if lab[r][c] == 0 and visited[r][c] == -1:
                return float('inf')
    return max_time

result = find_rumtime(N,M,lab)
print(result)