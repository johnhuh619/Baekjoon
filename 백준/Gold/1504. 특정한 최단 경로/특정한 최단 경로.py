import heapq
n, e = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges[a].append((b, cost))
    edges[b].append((a, cost))
v1, v2 = map(int, input().split())
INF = int(1e9)

def djikstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        cost, node = heapq.heappop(pq)
        
        if cost > dist[node]:
            continue
        
        for nxt, nc in edges[node]:
            new_cost = nc + cost
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    return dist
d_start = djikstra(1)
d_v1 = djikstra(v1)
d_v2 = djikstra(v2)

p1 = d_start[v1] + d_v1[v2] + d_v2[n]
p2 = d_start[v2] + d_v2[v1] + d_v1[n]
ans = min(p1,p2)

print(ans if ans < INF else -1)