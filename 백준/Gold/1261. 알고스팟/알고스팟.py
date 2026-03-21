import heapq
m, n = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

INF = int(1e9)
dist = [[INF] * m for _ in range(n)]
dist[0][0] = 0

pq = []
heapq.heappush(pq,(0,0,0))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while pq:
    w, x, y = heapq.heappop(pq)

    if dist[x][y] < w:
        continue
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            nw = w + board[nx][ny]

            if nw < dist[nx][ny]:
                dist[nx][ny] = nw
                heapq.heappush(pq, (nw, nx, ny))

print(dist[n-1][m-1])