import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
deg = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    deg[b] += 1


pq = []

for i in range(1, n+1):
    if deg[i] == 0:
        heapq.heappush(pq, i)

ans = []

while pq:
    cur = heapq.heappop(pq)
    ans.append(cur)
    
    for nxt in graph[cur]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            heapq.heappush(pq, nxt)
    
print(*ans)