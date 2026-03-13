n, m = map(int, input().split())

graph = []

for i in range(m):
    u, v, w = map(int, input().split())
    graph.append((w, u, v))

graph.sort()

parent = list(range(n+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    ra = find(a)
    rb = find(b)
    
    if ra == rb:
        return False
    
    parent[rb] = ra
    return True

tot = 0
max_w = 0

for w, u, v in graph:
    if union(u,v):
        tot += w
        max_w = w
        
ans = tot - max_w
print(ans)