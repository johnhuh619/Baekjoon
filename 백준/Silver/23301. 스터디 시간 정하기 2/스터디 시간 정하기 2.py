import sys
input = sys.stdin.readline
N, T = map(int, input().split())
av = [0] * 1001
for _ in range(N):
    k = int(input())
    for _ in range(k):
        s, e = map(int, input().split())
        av[s] += 1
        av[e] -= 1

for i in range(1, 1001):
    av[i] += av[i-1]
    
cur = sum(av[0:T])
top_sum = cur
top_st = 0

for s in range(1, 1001 - T + 1):
    # cur = sum(av[s:s+T])
    cur = cur - av[s-1] + av[s-1+T]
    if cur > top_sum:
        top_sum = cur
        top_st = s

print(top_st, top_st+T)      
    
    