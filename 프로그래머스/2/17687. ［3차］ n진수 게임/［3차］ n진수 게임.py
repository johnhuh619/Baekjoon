from collections import deque
def change(n, num):
    if num == 0:
        return "0"
    digits = "0123456789ABCDEF"
    s = []
    while num > 0:
        s.append(digits[num%n])
        num //= n
    return ''.join(reversed(s))

def solution(n, t, m, p):
    stream = []
    cur = 0
    while len(stream) < t*m:
        for ch in change(n, cur):
            stream.append(ch)
        cur += 1
    return ''.join(stream[p-1:t*m:m])
