def solution(s):
    n = len(s)
    answer = n
    
    for k in range(1, n//2+1):
        # k 를 커팅 단위 개수
        comp = ""
        prev = s[0:k]
        cnt = 1
        for i in range(k, n, k):
            cur = s[i:i+k]
            if cur == prev:
                cnt += 1
            else:
                comp += (str(cnt) if cnt > 1 else "") + prev
                prev = cur
                cnt = 1

        comp += (str(cnt) if cnt > 1 else "") + prev
        answer = min(answer, len(comp))
        
    return answer