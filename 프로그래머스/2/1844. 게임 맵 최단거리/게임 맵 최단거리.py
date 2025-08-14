from collections import deque

def bfs(start: tuple, map: list):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    r, c = len(map), len(map[0])
    q = deque([start])

    while q:
        x,y = q.popleft()

        # 벽 = 0
        # 길 = 1
        # 길에 누적하여 방문 추적
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c and map[nx][ny] == 1:
                map[nx][ny] = map[x][y] + 1
                q.append((nx, ny))
                if nx == r-1 and ny == c-1:
                    return map[nx][ny]
    return -1
def solution(maps):  
    return bfs((0,0), maps)