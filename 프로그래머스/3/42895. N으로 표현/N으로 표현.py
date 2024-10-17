def solution(N, number):
    answer = -1
    dp = []
    # 보통 첫 원소 idx = 0 , 이 함수에서는 idx = 1 /  why? 1~9
    for i in range(1, 9):
        current = []
        # N을 i번 반복한 숫자 추가
        current.append(int(str(N)*i))

        # 이전 단계의 숫자들과 조합하여 새로운 숫자 생성
        for j in range(1,i):
            for op1 in dp[j-1]:
                for op2 in dp[i-j-1]:
                    current.append(op1 + op2)
                    current.append(op1 - op2)
                    current.append(op2 - op1)
                    current.append(op1 * op2)
                    if op2 != 0:
                        current.append(op1 // op2)
                    if op1 != 0:
                        current.append(op2 // op1)
                    
        dp.append(list(set(current)))
        if number in dp[i-1]:
            answer = i
            break
    return answer