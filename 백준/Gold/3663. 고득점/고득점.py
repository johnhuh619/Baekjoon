def solution(name):
    up_down_cnt = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)
    n = len(name)
    min_move = n - 1
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        min_move = min(min_move, i*2 + n - next_idx, i + 2 * (n - next_idx))
    return up_down_cnt + min_move
    
n = int(input())
for _ in range(n):
    name = str(input())
    print(solution(name))