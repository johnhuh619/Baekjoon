from collections import defaultdict
n, m = map(int, input().split())

dic_team = defaultdict(list)
dic_name = {}
for _ in range(n):
    team = input()
    num = int(input())
    for _ in range(num):
        name = input()
        dic_name[name] = team
        dic_team[team].append(name)
    dic_team[team].sort()
for _ in range(m):
    quiz = input()
    t = int(input())
    if t == 0:
        for mem in dic_team[quiz]:
            print(mem)
    else:
        print(dic_name[quiz])
        
