import sys
sys.setrecursionlimit(1000000)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int,input().split())
parent = [i for i in range(n+1)]
    
for _ in range(m):
    k, a, b = map(int,input().split())
    if k == 0:
        union(a,b)
    if k == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")