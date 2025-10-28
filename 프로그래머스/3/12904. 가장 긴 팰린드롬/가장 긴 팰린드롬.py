def solution(s):
    n = len(s)
    if n < 2:
        return n
    
    max_len = 1
    
    def expand(l,r):
        nonlocal max_len
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        cur = r - l -1
        if max_len < cur:
            max_len = cur
    
    for i in range(n):
        expand(i, i)
        expand(i, i+1)
        
    return max_len