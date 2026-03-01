import sys
from collections import deque
board = [list(sys.stdin.readline().strip()) for _ in range(12)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# while True:
#     1. bfs로 모든 그룹 탐색
#     2. 4개 이상 그룹 제거
#     3. 제거된게 없다? 종료
#     4. 중력 적용
#     5. 연쇄 += 1
    
def bfs(x, y, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    color = board[x][y]
    group = [(x,y)]
    
    while q:
        cx, cy = q.popleft()    
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    group.append((nx,ny))
    
    return group


def gen_gravity():
    for col in range(6):
        stack = []
        for row in range(12):
            if board[row][col] != '.':
                stack.append(board[row][col])
            
        for row in range(11, -1, -1):
            if stack:
                board[row][col] = stack.pop()
            else:
                board[row][col] = '.'

chain = 0

while True:
    visited = [[False]*6 for _ in range(12)]
    explode = False
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, visited)
                if len(group) >= 4:
                    explode = True
                    for x, y in group:
                        board[x][y] = '.'
    if not explode:
        break
    
    gen_gravity()
    chain += 1

print(chain)
    