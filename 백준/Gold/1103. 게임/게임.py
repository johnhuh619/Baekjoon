import sys
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y):
    if visited[x][y]:
        print(-1)
        sys.exit()
        
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    visited[x][y] = True
    dp[x][y] = 1
    
    mv = int(board[x][y])
    
    for i in range(4):
        nx = x + dx[i]*mv
        ny = y + dy[i]*mv
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] != "H":
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    visited[x][y] = False
    return dp[x][y]

print(dfs(0,0))