def solution(N, stages):
    ans = [0] * (N+2)
    
    for s in stages:
        ans[s] += 1
    
    cnt = len(stages)
    answer = []
    
    for i in range(1,N+1):
        if cnt > 0:
            v = ans[i] / cnt
        else:
            v = 0
        cnt -= ans[i]
        answer.append((i,v))
    
    answer.sort(key=lambda x: (-x[1],x[0]))
        
    return [s for s, _ in answer]