import heapq

T = int(input())
INF = int(1e9)
def djikstra(start, edges, n):
    pq = [(0, start)]
    dist = [INF] * (n+1)
    dist[start] = 0
    while pq:
        cost, node = heapq.heappop(pq)

        if cost > dist[node]:
            continue
        
        for new_cost, nxt_node in edges[node]:
            nc = new_cost + dist[node]
            if nc < dist[nxt_node]:
                dist[nxt_node] = nc
                heapq.heappush(pq, (nc, nxt_node))
    
    return dist

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        edges[b].append((d,a))
        edges[a].append((d,b))
        if (a == g and b == h) or (a == h and b == g):
            dist_gh = d
        
    ends = []
    for _ in range(t):
        x = int(input())
        ends.append(x)
    ends.sort()

    dist_start = djikstra(s, edges, n)
    dist_g = djikstra(g, edges, n)
    dist_h = djikstra(h, edges, n)
    
    ans = []
    for e in ends:
        p1 = dist_start[g] + dist_gh + dist_h[e]
        p2 = dist_start[h] + dist_gh + dist_g[e]
        if dist_start[e] == p1 or dist_start[e] == p2:
           ans.append(e) 
    
    print(*ans)
    
