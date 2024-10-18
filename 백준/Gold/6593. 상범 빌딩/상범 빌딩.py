from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append((*start,0))
    visited[start[0]][start[1]][start[2]] = 1
    
    direction =  [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]  # 6 방향
    while queue:
        z, x, y, time = queue.popleft()
        if (z,x,y) == end:
            return time
        for dz, dx, dy in direction:
            nz = z + dz
            nx = x + dx
            ny = y + dy
            if 0<= nz < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[nz][nx][ny] and cube[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = 1
                    queue.append((nz,nx,ny, time + 1))

    return -1


while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0,0,0):
        break
    cube = []
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    start = None
    end = None

    for i in range(L):
        floor = []
        for j in range(R):
            row = input()
            floor.append(row)
            if 'S' in row:
                start = (i,j,row.index('S'))
            if 'E' in row:
                end = (i,j,row.index('E'))
        cube.append(floor)
        input()

    result = bfs(start,end)
    if result == -1:
        print("Trapped!")
    else:
        print(f'Escaped in {result} minute(s).')
