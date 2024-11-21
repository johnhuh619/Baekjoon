N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
dp[0] = points[0]
for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + points[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + points[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + points[i][2]

ans = min(dp[N-1])
print(ans)    