n = int(input())
dic = {}
for _ in range(n):
    name = input()
    dic[name] = dic.get(name, 0) + 1

for _ in range(n-1):
    sucess = input()
    dic[sucess] -= 1
    if dic[sucess] == 0:
        del dic[sucess]

for i in dic.keys():
    print(i)
