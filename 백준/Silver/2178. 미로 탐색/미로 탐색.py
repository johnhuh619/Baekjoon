# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다.
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.
from collections import deque
def sol():
    N, M = map(int, input().split())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    def bfs():
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        q = deque([(0,0,1)])
        while q:
            x, y, val = q.popleft()
            if x == N-1 and y == M-1:
                return val
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0<= ny < M:
                    if maze[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, val+1))
        return -1
    print(bfs())    
    
sol()
