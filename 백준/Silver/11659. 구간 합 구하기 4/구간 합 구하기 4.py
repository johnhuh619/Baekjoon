import sys
n,m = map(int,input().split())
num = list(map(int, input().split()))
res = [0]
totsum = 0
for i in range(n):
    totsum += num[i]
    res.append(totsum)

for _ in range(m):
    u,v = map(int,input().split())
    print(abs(res[v]-res[u-1]))


