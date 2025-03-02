def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for i in range(n+1)]    
    dp[1][1] = 1
    # right, down 
    # 격자에 가능한 경로 개수 넣기
    # 주변 격자의 값 (left, up)
    puddles = [(x,y) for (y,x) in puddles]
    for i in range(1, n+1): # row
        for j in range(1,m+1): # col
            if i == 1 and j == 1:
                continue
            if (i,j) in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])
    
    answer = dp[n][m] % 1000000007
    return answer