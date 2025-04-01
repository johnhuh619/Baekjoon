import sys
import heapq
a, b = map(int, input().split())
graph = [[] for _ in range(a+1)]

for _ in range(b):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))
    graph[e].append((s, v))


v1, v2 = map(int, input().split())

def dijkstra(start, end):
    route = [sys.maxsize]*(a+1)
    route[start] = 0
    q = [(0, start)]
    while q:
        tot_w, now = heapq.heappop(q)

        if route[now] < tot_w:
            continue

        for n_node, weight in graph[now]:
            cost = tot_w + weight
            if cost < route[n_node]:
                route[n_node] = cost
                heapq.heappush(q, (cost, n_node))
    return route[end]


r1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, a)
r2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, a)

if r1 >= sys.maxsize and r2 >= sys.maxsize:
    print(-1)
else:
    print(min(r1,r2))