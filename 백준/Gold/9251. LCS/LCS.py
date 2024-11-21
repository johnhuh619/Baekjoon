A, B = input(), input()
a, b = len(A), len(B)
dp = [[0]*(b+1) for _ in range(a+1)]

max_length = 0

for i in range(1, a+1):
    for j in range(1, b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if max_length < dp[i][j]:
                max_length = dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max_length)
            