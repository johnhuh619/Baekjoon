A, B = input(), input()
a, b = len(A), len(B)

dp = [[0]*(b+1) for _ in range(a+1)]

max_length = 0
end_indx = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_indx = i
                    
print(max_length)

