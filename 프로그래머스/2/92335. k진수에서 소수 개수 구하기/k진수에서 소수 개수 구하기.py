def make(num, k):
    s = []
    digits = '0123456789ABCDEF'
    while num > 0:
        s.append(digits[num%k])
        num //= k
    return ''.join(reversed(s))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = -1
    
    num = make(n, k)
    parts = num.split('0')
    cnt = 0
    for p in parts:
        if p != '' and is_prime(int(p)):
            cnt += 1
    return cnt