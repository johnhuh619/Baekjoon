t = int(input())
for i in range(t):
    n = int(input())
    wear = {}
    for j in range(n):
        cloth = list(input().split())
        if cloth[1] in wear:
            wear[cloth[1]].append(cloth[0])
        else:
            wear[cloth[1]] = [cloth[0]]
    cnt = 1
    for k in wear:
        cnt *=(len(wear[k])+1)
    print(cnt -1) # all 0 일때 제외