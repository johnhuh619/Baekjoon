import heapq
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
v1, v2 = map(int, input().split())

# 1 -> v1 -> v2 -> N
# 1 -> v2 -> v2 -> N


def djikstar(start):
    cap = [1e9] * (n+1)
    pq = [(0, start)]
    cap[start] = 0
    while pq:
        cw, cn = heapq.heappop(pq)
        
        if cw > cap[cn]:
            continue
        
        for nxt_node, nxt_w in graph[cn]:
            cur_w = nxt_w + cw
            if  cur_w < cap[nxt_node]:
                cap[nxt_node] = cur_w
                heapq.heappush(pq,(cur_w, nxt_node))
    return cap


cap1 = djikstar(1)
cap_v1 = djikstar(v1)
cap_v2 = djikstar(v2)
case1 = cap1[v1] + cap_v1[v2] + cap_v2[n]
case2 = cap1[v2] + cap_v2[v1] + cap_v1[n]

ans = min(case1, case2)
print(ans if ans < 1e9 else -1)