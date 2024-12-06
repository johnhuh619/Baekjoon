N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dp = [[[0]*N for _ in range(N)] for _ in range(3)]


dp[0][0][1] = 1

for i in range(N):
    for j in range(N):
        if j+1 < N and graph[i][j+1] == 0:  # 가로 이동
            dp[0][i][j+1] += dp[0][i][j]
            dp[0][i][j+1] += dp[2][i][j]
        if i+1 < N and graph[i+1][j] == 0:  # 세로 이동
            dp[1][i+1][j] += dp[1][i][j]
            dp[1][i+1][j] += dp[2][i][j]
        if i+1 < N and j+1 < N and graph[i][j+1] == 0 and graph[i+1][j] == 0 and graph[i+1][j+1] == 0:
            dp[2][i+1][j+1] += dp[0][i][j]
            dp[2][i+1][j+1] += dp[1][i][j]
            dp[2][i+1][j+1] += dp[2][i][j]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])
