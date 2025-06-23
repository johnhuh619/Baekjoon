
# 모든 조합 구해서
# 시뮬레이션
from itertools import combinations
import heapq
def solution(k, n, reqs):
    answer = 0
    by_type = [[] for _ in range(k)]
    for a, b, c in reqs:
        by_type[c-1].append((a,b))
        
    def mentor_comb(k, n):
        base = [1]*k
        left_m = n- k
        res = []
        for bars in combinations(range(left_m + k - 1), k-1):
            parts = []
            prev = -1
            for b in bars:
                parts.append(b - prev - 1)
                prev = b
            parts.append(left_m+k-1 - prev -1)
            c = [base[i] + parts[i] for i in range(k)]            
            res.append(c)
        return res
    
    min_wait = float('inf')
    for mentor in mentor_comb(k,n):
        tot_wait = 0
        # 타입에 따른 대기시간 더하는 루프
        for t in range(k):
            n_mentors = mentor[t]
            req_list = by_type[t]
            
            can = [0]*n_mentors
            heapq.heapify(can)
            wait = 0
            for start, dur in req_list:
                finish = heapq.heappop(can)    
                if finish <= start:
                    heapq.heappush(can,start+dur)
                else:
                    wait+= finish - start
                    heapq.heappush(can,finish+dur)
            tot_wait += wait
        # 이번 조합에서의 대기시간이 최소인지 비교
        min_wait = min(min_wait, tot_wait)
    return min_wait