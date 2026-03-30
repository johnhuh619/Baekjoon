n = int(input())
m = int(input())
edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((w,a,b))

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
cnt = 0
for v, a, b in edges:   
    if union(a,b):
        ans += v
        cnt += 1
        if cnt == n-1:
            break
print(ans)