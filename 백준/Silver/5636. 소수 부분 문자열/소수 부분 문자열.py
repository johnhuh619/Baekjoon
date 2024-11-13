import sys


def era_find(limit):
    is_prime = [True]*(limit+1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2,int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, limit+1,i):
                is_prime[j] = False
    return is_prime

is_prime = era_find(100000)

def sliding_window(n):
    max_prime = -1
    for length in range(5,0,-1):
        for i in range(len(n) - length+1):
            num = int(n[i:i+length])
            if is_prime[num]:
                max_prime = max(max_prime,num)
        if max_prime != -1:
            break
    return max_prime

res = []
while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    res.append(sliding_window(n))

for res in res:
    print(res)
    