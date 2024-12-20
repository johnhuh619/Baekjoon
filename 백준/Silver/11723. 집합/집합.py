import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        f, x = temp[0], temp[1]
        x = int(x)

        if f == "add":
            S.add(x)
        elif f == "remove":
            S.discard(x)
        elif f == "check":
            print(1 if x in S else 0)
        elif f == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)