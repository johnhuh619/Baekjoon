
# f(n-1)
# f(n-2) 
# f(n-3) 
t = int(input())
test = list(int(input()) for _ in range(t))
dp = [0]*12
dp[1], dp[2], dp[3] = 1,2,4
for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for tc in test:
    print(dp[tc])
