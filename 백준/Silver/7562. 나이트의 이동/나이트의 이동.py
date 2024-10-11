from collections import deque

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

def bfs(start_x, start_y, target_x, target_y):
    queue = deque()
    queue.append((start_x,start_y))
    while queue:
        curX, curY = queue.popleft()
        if curX == target_x and curY == target_y:
            print(visited[curX][curY] - 1)
            return True
        
        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[curX][curY] + 1
                queue.append((nx,ny))
    return False    

N = int(input())
for i in range(N):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    visited[start_x][start_y] = 1
    bfs(start_x,start_y,target_x,target_y)