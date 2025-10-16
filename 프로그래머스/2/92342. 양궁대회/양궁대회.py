def solution(n, info):
    result = [-1]
    max_diff = 0
    
    def dfs(idx, remain, lion):
        nonlocal result, max_diff
        
        if idx == 11 or remain == 0:
            lion = lion[:]
            if remain > 0:
                lion[10] += remain
            
            f_score, l_score = 0, 0
            for i in range(11):
                if info[i] == lion[i] == 0:
                    continue

                if lion[i] > info[i]:
                    l_score += 10 - i

                else:
                    f_score += 10 - i

            diff = l_score - f_score

            # 만약 작다면 return ("")
            if diff <= 0:
                return

            if diff > max_diff:
                max_diff = diff
                result = lion
            elif diff == max_diff:
                for i in range(10, -1, -1):
                    if lion[i] > result[i]:
                        result = lion
                        break
                    elif lion[i] < result[i]:
                        break
            return

        # 현재 사용한 화살
        need = info[idx] + 1

        if remain >= need:
            lion[idx] = need
            dfs(idx + 1, remain - need, lion)
            lion[idx] = 0

        dfs(idx+1, remain, lion)
    dfs(0,n,[0]*11)
        
    return result


# 어피치 n발을 다 쐈다.
# info => 어피치 점수. 
# 화살 개수 n
# 10 9 8 7 6 5 4 3 2 1

# 가장 큰 점수 차로 이겨야 하낟. 

# n 발의 화살을 어떻게 배분해서 어떻게 이길 거냐. 
# 누적시키기?

# 완전 탐색? 


    