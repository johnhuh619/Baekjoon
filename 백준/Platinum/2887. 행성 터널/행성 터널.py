n = int(input())
nodes = []
for i in range(n):
    x, y, z = map(int, input().split())
    nodes.append((i, x, y, z))

dist = [[] * n for _ in range(n)]

edges = []
nodes.sort(key=lambda x: x[1])
for i in range(n-1):
    a_idx, ax, ay, az = nodes[i]
    b_idx, bx, by, bz = nodes[i+1]
    edges.append((abs(ax-bx), a_idx, b_idx))

nodes.sort(key=lambda x: x[2])
for i in range(n-1):
    a_idx, ax, ay, az = nodes[i]
    b_idx, bx, by, bz = nodes[i+1]
    edges.append((abs(ay-by), a_idx, b_idx))

nodes.sort(key=lambda x: x[3])
for i in range(n-1):
    a_idx, ax, ay, az = nodes[i]
    b_idx, bx, by, bz = nodes[i+1]
    edges.append((abs(az-bz), a_idx, b_idx))

edges.sort()

# union / find
parent = list(range(n))
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
        parent[rb] = ra
    else:
        parent[ra] = rb

    return True

ans = 0
cnt = 0

for cost, a, b in edges:
    if union(a,b):
        ans += cost
        cnt += 1
        if cnt == n-1:
            break

print(ans)
