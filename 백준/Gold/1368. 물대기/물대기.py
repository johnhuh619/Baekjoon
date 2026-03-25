n = int(input())
edges = []

for i in range(1, n+1):
    w = int(input())
    edges.append((w, 0, i))
    
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(1, n+1):
        if i < j:
            edges.append((data[j-1], i, j))
    

parent = list(range(n+1))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
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

edges.sort()
for cost, a, b in edges:
    if union(a,b):
        ans += cost
        cnt += 1
        if cnt == n:
            break
print(ans)