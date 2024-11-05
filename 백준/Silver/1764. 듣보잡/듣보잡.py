n, m = map(int,input().split())
dic = {}

for _ in range(n):
    x = input()
    if x not in dic:
        dic[x] = 1

res =[]
for _ in range(m):
    y = input()
    if y in dic:
        res.append(y)
res.sort()
print(len(res))
for i in res:
    print(i)