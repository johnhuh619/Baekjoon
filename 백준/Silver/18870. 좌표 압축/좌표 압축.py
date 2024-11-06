import sys
n = int(input())
num = list(map(int,sys.stdin.readline().split()))
s = sorted(set(num))
dic = {s[i]: i for i in range(len(s))}
res = []
for v in num:
    res.append(dic[v])
print(*res)

