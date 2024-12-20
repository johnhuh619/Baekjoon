# (1-1) x % 2 = 0 -> 2
# (1-2) x % 3 = 0 -> 3
# (2) -1

n = int(input()) 
dp =[0]*(10**6+1)

for i in range(2, n+1):
    # 현재 수에서 -1
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
print(dp[n])