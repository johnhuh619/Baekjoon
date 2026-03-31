n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

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
    
    if ra < rb:
        parent[ra] = rb
    else:
        parent[rb] = ra
    
    return True

ans = 0
max_cost = 0
for cost, a, b in edges:
    if union(a, b):
       ans += cost
       max_cost = cost
ans = ans - max_cost    
print(ans) 
    
    