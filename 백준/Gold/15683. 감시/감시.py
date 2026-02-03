import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

arr = []
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            arr.append((i,j,board[i][j]))

 
# 0: up 1: down 2: left 3: right
dirs = [
    [],
    [[0],[1],[2],[3]],
    [[0,1], [2,3]],
    [[0,2], [2,1], [1,3], [3,0]],
    [[0,1,2], [0,1,3], [0,2,3], [1,2,3]],
    [[0,1,2,3]]
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def search(arr, x, y, d):
    nx, ny = x, y
    while True:
        nx += dx[d]
        ny += dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            break
        if arr[nx][ny] == 6:
            break
        if arr[nx][ny] == 0:
            arr[nx][ny] = -1
        
ans = float('inf')
def dfs(idx, board):
    global ans
    if idx == len(arr):
        nans = sum(row.count(0) for row in board)
        ans = min(ans, nans)
        return
    
    x, y, v = arr[idx]
    for dir in dirs[v]:
        n_board = [row[:] for row in board]
        for d in dir:
            search(n_board, x, y, d)
        dfs(idx + 1, n_board)
            
dfs(0,board)
print(ans)