from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque([(0,0,0)])
    visited[0][0][0] = 1
    
    while q:
        x, y, broken = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][broken]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    q.append((nx, ny, broken))
                
                elif board[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    q.append((nx, ny, 1))
    return -1

print(bfs())