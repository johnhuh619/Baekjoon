def solution(sequence, k):
    answer = []
    n = len(sequence)
    tot = 0
    s = 0
    min_len = n
    for e in range(n):
        tot += sequence[e]
        while tot > k:
            tot -= sequence[s]
            s += 1
        if tot == k and min_len > e-s:
            min_len = e-s
            answer = [s,e]
    
    return answer