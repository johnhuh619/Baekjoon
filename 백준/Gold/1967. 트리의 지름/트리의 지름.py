import sys
sys.setrecursionlimit(1000000)
def write_distance(start,cur):
    visited[start] = 1
    dist[start] = cur
    for node, w in tree[start]:
        if not visited[node]:
            write_distance(node,cur+w)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, n, w = map(int, input().split())
    tree[p].append((n,w))
    tree[n].append((p,w))
    
dist = [0]*(N+1)
visited = [0]*(N+1)

write_distance(1,0)
start = 1
for i in range(2,N+1):
    if dist[i] > dist[start]:
        start = i
        
dist = [0]*(N+1)
visited = [0]*(N+1)
write_distance(start,0)
print(max(dist))
