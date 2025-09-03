def sol():
    s = input()
    size = s.count('a')
    n = len(s)

    if size == n or size == 0: 
        return 0
    t = s + s
    b_cnt = t[:size].count('b')
    ans = b_cnt

    for i in range(n+1):
        if t[i] == 'b':
            b_cnt -= 1
        if t[i + size] == 'b':
            b_cnt += 1
        ans = min(ans, b_cnt)   
    return ans

print(sol())