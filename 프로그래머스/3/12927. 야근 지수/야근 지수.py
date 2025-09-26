# 야근 시작점 -> 남은 일의 작업량 ** 2
# 4,2,3

import heapq

def solution(n, works):
    answer = 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        max_works = heapq.heappop(works)
        if max_works == 0:
            break
        heapq.heappush(works, max_works+1)
    
        
    return sum(w * w for w in works)