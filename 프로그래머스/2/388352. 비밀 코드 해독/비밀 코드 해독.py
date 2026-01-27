from itertools import combinations
def solution(n, q, ans):
    answer = 0
    for comb in combinations(range(1,n+1), 5):
        comb_set = set(comb)    
        flag = True
        
        for i in range(len(q)):
            cnt = 0
            for c in q[i]:
                if c in comb_set:
                    cnt += 1
            if cnt != ans[i]:
                flag = False
                break
                
        if flag:
            answer += 1
    
    return answer