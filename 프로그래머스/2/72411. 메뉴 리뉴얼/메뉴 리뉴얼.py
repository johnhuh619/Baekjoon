# order는 순서가 필요 없음
# 그러므로 alphabetical order 로 정렬
# 정렬한 놈으로 조합 만들기
from collections import defaultdict

def solution(orders, course):
    def comb(arr, start, limit, path, result):
        if limit == 0:
            result.append(''.join(path))
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            comb(arr, i+1, limit-1, path, result)
            path.pop()
            
    res = []
    
    for limit in course:
        # n 에서 가능한 조합 전부 구함.
        freq = defaultdict(int)
        for order in orders:
            order = ''.join(sorted(order))
            combs = []
            comb(order, 0, limit, [], combs)
            
            for c in combs:
                freq[c] += 1
                
        if not freq:
            continue
            
        max_cnt = max(freq.values())
        if max_cnt < 2:
            continue
        
        for k, cnt in freq.items():
            if cnt == max_cnt:
                res.append(k)
                
    return sorted(res)