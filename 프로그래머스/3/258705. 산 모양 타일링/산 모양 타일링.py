# 사다리꼴의 윗변의 길이 n => n 칸
# 사다리꼴 윗변(2층) 에 부착한 삼각형을 나타내는 tops 가 존재 => t / n 점유
# 마름모는 3가지 위치 가능. 윗칸 O 3개 / 윗칸 X 2개
# 마름모는 삼각형 2개짜리. 
# 총 칸 수 = (2n + 1) + len(tops)
# 1. 삼각형 채우기
# 2. 좌/우 마름모로 채우기
# 3. 위 마름모로 채우기

def solution(n, tops):

    MOD = 10007
    
    dp = [[0,0] for _ in range(n)]

    # tops 기준 i번째 열까지 채울 때 넘어가지 않았을 때
    dp[0][0] = 3 if tops[0] == 1 else 2
    
    # tops 기준 i 번째 열까지 채울 때 오른쪽으로 넘어간 마름모일 때
    dp[0][1] = 1
    
    for i in range(1, n) :
        if tops[i] == 0:
            val_0, val_1 = 2, 1
        else:
            val_0, val_1 = 3, 2
    
        
        dp[i][0] = (dp[i-1][0] * val_0 + dp[i-1][1]*val_1) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD
        
    return (dp[n-1][0] + dp[n-1][1])%MOD