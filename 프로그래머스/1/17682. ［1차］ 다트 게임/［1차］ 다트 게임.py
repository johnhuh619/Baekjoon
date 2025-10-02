def solution(dartResult):
    scores = []
    i = 0
    n = len(dartResult)
    
    while i < n:
        # 숫자 (10 고려)
        if dartResult[i].isdigit():
            if i+1 < n and dartResult[i] == '1' and dartResult[i+1] == '0':
                num = 10
                i += 1
            else:
                num = int(dartResult[i])
        # 보너스 처리
        elif dartResult[i] in "SDT":
            if dartResult[i] == 'S':
                num **= 1
            elif dartResult[i] == 'D':
                num **= 2
            else:
                num **= 3
            scores.append(num)
        # 옵션 처리
        elif dartResult[i] in "*#":
            if dartResult[i] == '*':
                scores[-1] *= 2
                if len(scores) > 1:
                    scores[-2] *= 2
            else:
                scores[-1] *= -1
        i += 1
    
    return sum(scores)
