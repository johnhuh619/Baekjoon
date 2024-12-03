
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
P = int(input())
li = [list(map(int, input().split())) for _ in range(P)]
dp =[[0]*(M+1) for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, M+1):
        dp[x][y] = dp[x-1][y] + dp[x][y-1] + board[x-1][y-1] - dp[x-1][y-1]
        
for _, line in enumerate(li):
    i,j,x,y = line
    print(dp[x][y] - dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1])
