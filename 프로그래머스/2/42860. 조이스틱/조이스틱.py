def solution(name):
    # z <-> a-z <-> a
    # left 
    # 1. z->a , a->z 
    # 2. 64 다 빼기
    # min move 구하기 how?
    # if 값이 A가 아니고 and 거리가 가깝다면.
    
    up_down_cnt = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)
    n = len(name)
    min_move = n - 1
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        min_move = min(min_move, i*2 + n - next_idx, i + 2 * (n - next_idx))
    return up_down_cnt + min_move