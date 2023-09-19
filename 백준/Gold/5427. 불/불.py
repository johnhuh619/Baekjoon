from collections import deque
import sys
dx = [1,-1,0,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    visited[x][y] = 1
    q.append((x,y))
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
        
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < h and 0 <= ny< w:
                    if graph[nx][ny] == "." and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))
                elif nx < 0 or ny < 0 or nx >= h or ny >= w:
                    print(visited[x][y])
                    return
            qlen -= 1
        fire()
    print("IMPOSSIBLE")
    return

def fire():
    lenq = len(fq)
    while lenq:
        x,y = fq.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < h and 0 <= ny< w:
                if graph[nx][ny] == "." :
                    graph[nx][ny] = "*"
                    fq.append((nx,ny))
        lenq -=1
num = int(input())
for _ in range(num):
    w,h = map(int,input().split())
    graph = [list(sys.stdin.readline()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    # 사람 큐 불 큐
    q = deque()
    fq = deque()
    for i in range(h):
        for j in range(w):
            # 사람 찾기
            if graph[i][j] == "@":
                x,y = i,j
                graph[i][j] = '.'
            if graph[i][j] == "*":
                fq.append((i,j))
    fire()
    bfs(x,y)

