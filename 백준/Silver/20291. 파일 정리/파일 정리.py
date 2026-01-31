n = int(input())
dic = {}
for _ in range(n):
    file = input().rstrip()
    fname, ftype = file.split('.')
    dic[ftype] = dic.get(ftype, 0) + 1

for f in sorted(dic):
    print(f, dic[f])
    