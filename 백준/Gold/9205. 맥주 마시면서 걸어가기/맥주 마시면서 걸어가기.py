from collections import deque
def bfs():
    q = deque()
    q.append((x_h,y_h))
    while q:
        x, y = q.popleft()
        if abs(x-x_fes) + abs(y-y_fes) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = graph[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append((nx,ny))
                    visited[i] = 1
    print('sad')
    return



t = int(input())
for _ in range(t):
    n = int(input())
    x_h, y_h = map(int,input().split())
    graph = []
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x,y))
    x_fes, y_fes = map(int, input().split())
    visited = [0 for _ in range(n+1)]
    bfs()
