import heapq
m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)] 

INF = int(1e9)
pq = [(0,0,0)]
cost = [[INF]*m for _ in range(n)]
cost[0][0] = 0

dx = [1, -1, 0, 0]
dy = [0,0,1,-1]

while pq:
    c, x, y = heapq.heappop(pq)
    
    if c > cost[x][y]:
        continue
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            nc = graph[nx][ny] + c
            if nc < cost[nx][ny]:
                cost[nx][ny] = nc
                heapq.heappush(pq,(nc, nx, ny))

print(cost[n-1][m-1])