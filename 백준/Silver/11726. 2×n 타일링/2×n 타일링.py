# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 5
# f(5) = 8
dp = [0]*1001
dp[1], dp[2] = 1, 2
n = int(input())
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)