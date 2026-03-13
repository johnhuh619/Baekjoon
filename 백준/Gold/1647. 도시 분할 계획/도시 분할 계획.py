import heapq
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

visited = [False] * (n+1)
pq = [(0,1)]

tot = 0
max_w = 0
cnt = 0

while pq:
    cw, cn = heapq.heappop(pq)
    
    if visited[cn]:
        continue
    
    visited[cn] = True
    tot += cw
    max_w = max(max_w, cw)
    cnt += 1
    
    for nw, nn in graph[cn]:
        if not visited[nn]:
            heapq.heappush(pq, (nw, nn))
        

ans = tot - max_w
print(ans)