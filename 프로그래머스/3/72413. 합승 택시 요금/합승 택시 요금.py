import heapq

def djikstra(n, start, graph):
    dist = [float('inf')]  * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        
        for nxt, w in graph[node]:
            totw = cost + w
            if totw < dist[nxt]:
                dist[nxt] = totw
                heapq.heappush(pq,(totw, nxt))
    return dist
    
def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for sn, en, w in fares:
        graph[sn].append((en,w))
        graph[en].append((sn,w))
    
    dist_s = djikstra(n, s, graph)
    dist_a = djikstra(n, a, graph)
    dist_b = djikstra(n, b, graph)
    
    min_cost = float('inf')
    for i in range(1, n+1):
        n = dist_s[i] + dist_a[i] + dist_b[i]
        min_cost = min(min_cost, n)
        
    return min_cost