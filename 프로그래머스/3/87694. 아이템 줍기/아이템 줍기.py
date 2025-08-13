from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    # 지도를 구축한다
    
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for r in rectangle:
        x1, y1, x2, y2 = r[0]*2, r[1]*2, r[2]*2, r[3]*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1<i<x2 and y1<j<y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
                    
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    
    q = deque([(cx,cy)])
    while q:
        x, y = q.popleft()
        if x == ix and y == iy:
            break
        
        for i in range(4):
            nx = x + dx[i]                
            ny = y + dy[i]
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                q.append((nx,ny))
    return visited[ix][iy] // 2