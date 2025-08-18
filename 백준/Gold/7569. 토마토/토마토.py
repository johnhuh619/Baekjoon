from collections import deque


    




def sol():
    # row, col, height
    m, n, h = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    
    #bfs
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    q.append((i,j,k))
                    
    while q:
        z, y, x = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < m and 0 <= ny < n and 0<= nz < h and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                q.append((nz,ny,nx))
    
    ans = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                t = box[z][y][x]                                    
                if  t == 0:
                    return -1
                    
                if t == -1:
                    continue
                ans = max(ans, t)
    return (ans - 1)


print(sol())
    