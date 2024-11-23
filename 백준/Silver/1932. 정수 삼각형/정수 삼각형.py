n = int(input())
dp=[[0]*n for _ in range(n)]
tri = []
for _ in range(n):
  tri.append(list(map(int,input().split())))
dp[0][0] = tri[0][0]
for i in range(1,n):
  for j in range(0,i+1):
    if j == 0:
      dp[i][j] = dp[i-1][j] + tri[i][j]
    elif j == i+1:
      dp[i][j] = dp[i-1][j-1] + tri[i][j]
    else:
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + tri[i][j]

print(max(dp[n-1]))
  

