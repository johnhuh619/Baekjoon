import heapq

T = int(input())
INF = int(1e9)
def djikstra(start, edges, n):
    pq = [(0,start)]
    dist = [INF] * (n+1)
    dist[start] = 0
    
    while pq:
        cost, cur = heapq.heappop(pq)
        if dist[cur] < cost:
            continue
        
        for nxt, nc in edges[cur]:
            new_cost = nc + dist[cur]
            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    return dist
    
    
for _ in range(T):
    # 교차로/ 도로/ 목적지
    n, m, t = map(int, input().split())

    # s = start / g <-> h = 지나간 edge 1개
    s, g, h = map(int, input().split())
    
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        # a <-> b = d
        a, b, d = map(int, input().split())
        edges[a].append((b, d))
        edges[b].append((a, d))
        if (a == g and b == h) or (a == h and b == g):
            gh_dist = d
        
    end = []
    for _ in range(t):
        x = int(input())
        end.append(x)
        
    end.sort()

    dist_start = djikstra(s, edges, n)
    dist_g = djikstra(g, edges, n)
    dist_h = djikstra(h, edges, n)
    
    ans = []
    
    for x in end:
        p1 = dist_start[g] + gh_dist + dist_h[x]
        p2 = dist_start[h] + gh_dist + dist_g[x]
        
        if dist_start[x] == p1 or dist_start[x] == p2:
            ans.append(x)
    
    print(*ans)
        