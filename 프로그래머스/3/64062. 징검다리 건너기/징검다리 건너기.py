# 최대 이동 거리 = k
# dfs를 while문 안에서 돌려서 최대 개수를 찾아야 하나?
# 아니. "다음으로 밟을 수 있느 디딤돌 다수이면, 가장 가까운 디딤돌로만 이동"
# 그렇다면 이동 하다 k 넘어야 하는 상황이 오면 종료해야 한다.
# 단순 for문으로 하면 안되나? 안된다. 
# 한번에 구해야한다.
# 윈도우 size = k 윈도우 내 최댓값이 윈도우 내 버틸 수 있는 최대 인원수
# 최대 인원 수 모음에서 가장 작은 값이 가능한 최대 인원
from collections import deque

def solution(stones, k):
    dq = deque()
    min_or_max = float('inf')
    
    for i, v in enumerate(stones):
        while dq and stones[dq[-1]] <= v:
            dq.pop()
        dq.append(i)
    
        if dq[0] <= i-k:
            dq.popleft()

        if i >= k -1:
            min_or_max = min(min_or_max, stones[dq[0]])
    
    return min_or_max