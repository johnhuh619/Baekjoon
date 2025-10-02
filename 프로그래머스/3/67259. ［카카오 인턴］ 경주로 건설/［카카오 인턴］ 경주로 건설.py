# 1 코너 = 5 직선
import heapq

def solution(board):
    n = len(board)
    INF = float('inf')
    visited = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    
    pq = []
    # 하, 상, 우, 좌
    # 0,  1,  2, 3
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for d in [0,2]:
        visited[0][0][d] = 0
        heapq.heappush(pq, (0,0,0,d)) # cost, x, y, dir
    
    while pq:
        cost, x, y, dir = heapq.heappop(pq)
        
        if cost > visited[x][y][dir]:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                # 직선
                if dir == i:
                    nc = cost + 1
                # 코너
                else:
                    nc = cost + 6
                
                if visited[nx][ny][i] > nc:
                    visited[nx][ny][i] = nc
                    heapq.heappush(pq, (nc, nx, ny, i))
                
    return min(visited[n-1][n-1]) * 100
