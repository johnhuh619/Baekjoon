def solution(sequence):
    answer = 0
    n = len(sequence)
    pulse1 = [ (-1)**(i+1) for i in range(n)]
    pulse2 = [ (-1)**(i+2) for i in range(n)]
    
    seq1 = [a*p for a, p in zip(sequence, pulse1)]
    seq2 = [b*p for b, p in zip(sequence, pulse2)]
    
    max_sum1 = cur_sum = seq1[0]
    for x in seq1[1:]:
        cur_sum = max(cur_sum+x, x)
        max_sum1 = max(max_sum1, cur_sum)
    
    max_sum2 = cur_sum = seq2[0]
    for y in seq2[1:]:
        cur_sum = max(cur_sum+y, y)
        max_sum2 = max(max_sum2, cur_sum)
        
    return max(max_sum1, max_sum2)