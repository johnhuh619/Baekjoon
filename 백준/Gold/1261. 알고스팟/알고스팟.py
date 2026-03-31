import heapq
n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(m)]

def djikstra():
    INF = int(1e9)
    pq = [(0,0,0)]
    costs = [[INF]*(n) for _ in range(m)]
    costs[0][0] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while pq:
        cost, x, y = heapq.heappop(pq)
        if cost > costs[x][y]:
            continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                nc = cost + board[nx][ny]
                if nc < costs[nx][ny]:
                    costs[nx][ny] = nc
                    heapq.heappush(pq, (nc, nx, ny))
    
    return costs

arr = djikstra()
print(arr[m-1][n-1])
