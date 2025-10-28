def solution(sticker):
    answer = 0
    
    # 1 떼면 항상 n-1 뗼 수 없음.
    # 1 을 안떼었다면, n-1 뗼수도/ 없을 수도
    
    n = len(sticker)
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker)
    
    # 1번 포함
    dp1 = [0]*n
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0],sticker[1])
    
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    dp2 = [0]*n
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
        
    return max(dp1[n-2], dp2[n-1])