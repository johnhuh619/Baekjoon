n, m = map(int, input().split())
graph = []
for _ in range(m):
    u, v, w = map(int, input().split())
    graph.append((w,u,v))
graph.sort()

parent = list(range(n+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(u,v):
    u_name = find(u)
    v_name = find(v)

    if u_name != v_name:
        parent[u_name] = v_name
        return True
    return False



ans = 0
cnt = 0
for w, u, v in graph:
    if union(u,v):
        ans += w
        cnt += 1
        if cnt == n-1:
            break

print(ans)