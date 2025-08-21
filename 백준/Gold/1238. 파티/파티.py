import heapq

INF = int(1e9)



def sol():
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, val = map(int,input().split())
        graph[start].append((end, val))
    
    
    def djikstra(start):
        q = []
        dist = [INF]*(N+1)
        dist[start] = 0
            
        heapq.heappush(q, (0, start))
            
        while q:
            val, node = heapq.heappop(q)
            
            if dist[node] < val:
                continue
            
            for nNode_idx, nNode_val in graph[node]:
                nxt_val = nNode_val + val
                if dist[nNode_idx] > nxt_val:
                    dist[nNode_idx] = nxt_val
                    heapq.heappush(q, (nxt_val, nNode_idx))
                    
        return dist
    
    res = 0
    from_x = djikstra(X)
    
    for i in range(1, N+1):
        to_x = djikstra(i)
        res = max(res, (to_x[X] + from_x[i]))
    
    return res

print(sol())