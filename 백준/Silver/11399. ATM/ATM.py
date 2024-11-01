n = int(input())
num = list(map(int,input().split()))
num.sort()
dp = [0]*(n)

dp[0] = num[0]
for i in range(1,n):
    dp[i] = dp[i-1] + num[i]
print(sum(dp))

