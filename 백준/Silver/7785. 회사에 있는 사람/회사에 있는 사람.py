n = int(input())
com = set()
for _ in range(n):
    name, log = input().split()
    if log == "enter":
        com.add(name)
    else:
        com.remove(name)
c = list(com)
c.sort(reverse=True)
for p in c:
    print(p)