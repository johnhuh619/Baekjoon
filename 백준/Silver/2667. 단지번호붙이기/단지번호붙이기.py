from collections import deque

n = int(input())
graph= [list(map(int,input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    q = deque([(x,y)])
    graph[x][y] += 1
    size = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                    size += 1
                    graph[nx][ny] += 1
                    q.append((nx, ny))

    return size    

arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            arr.append(bfs(i,j))

arr.sort()
print(len(arr))
for i in arr:
    print(i)


