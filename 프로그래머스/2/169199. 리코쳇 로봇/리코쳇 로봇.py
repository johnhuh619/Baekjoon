# d는 장애물.
# 장애물을 마주치면 방향전환
# 방향전환 => -1,+1

from collections import deque

def solution(board):
    answer = 0
    r = len(board)
    c = len(board[0])
    start_row, start_col = 0, 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                start_row, start_col = i, j
    start = [start_row, start_col]
    cnt = bfs(start, r, c, board)
    
    return cnt

def bfs(start, row, col, board):
    q = deque()
    q.append((start[0], start[1], 0))
    
    visit = [ [0]*col for _ in range(row) ]
    visit[start[0]][start[1]] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        cx, cy, cnt = q.popleft()
        if board[cx][cy] == 'G':
            return cnt
        for i in range(4):
            nx, ny = cx, cy
            while True:
                tx, ty = nx + dx[i], ny +dy[i]
            
                if 0 <= tx < row and 0 <= ty < col and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
            if visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx, ny, cnt+1))
    return -1
        
    
    
    