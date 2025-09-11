from collections import deque
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs():
    mcnt = 0
    stack = deque([(0,0,graph[0][0])])    

    while stack:
        x, y, route = stack.pop()
        mcnt = max(mcnt, len(route))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] not in route:
                    stack.append((nx, ny, route + graph[nx][ny]))
    return mcnt
print(dfs())             
