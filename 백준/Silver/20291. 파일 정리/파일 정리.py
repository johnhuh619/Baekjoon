n = int(input())
dic = {}
for _ in range(n):
    fname, typ = map(str, input().split('.'))
    dic[typ] = dic.get(typ, 0) + 1

for f in sorted(dic):
    print(f, dic[f])