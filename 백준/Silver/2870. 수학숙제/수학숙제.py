import re

t = int(input())
res = []
for _ in range(t):
    test = input()
    p = re.compile('[0-9]+')
    m = p.findall(test)
    for i in m:
        res.append(int(i))
res.sort()
for j in res:
    print(j)