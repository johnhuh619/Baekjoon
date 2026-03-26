import heapq

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))
    rev_graph[b].append((a,w))


INF = int(1e9)
def djikstra(start, graph):
    dist = [INF] * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, cur = heapq.heappop(pq)
        if dist[cur] < cost:
            continue
        
        for nxt, nc in graph[cur]:
            new_cost = nc + cost
            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    return dist

go = djikstra(x, graph)
back = djikstra(x, rev_graph)

max_dist = 0
for i in range(1, n+1):
    max_dist = max(go[i] + back[i], max_dist)

print(max_dist)