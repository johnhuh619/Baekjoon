import sys
import heapq
INF = sys.maxsize
n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n+1)]
route = [INF]*(n+1)

for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

def dijkstsra(start):
    route[start] = 0
    pq = [(0,start)]
    while pq:
        tot_w, now = heapq.heappop(pq)
        if route[now] < tot_w:
            continue
        for n_node, weight in graph[now]:
            cost = tot_w + weight
            if cost < route[n_node]:
                route[n_node] = cost
                heapq.heappush(pq, (cost, n_node))

dijkstsra(k)


for i in range(1,n+1):
    print(route[i] if route[i] != INF else "INF")