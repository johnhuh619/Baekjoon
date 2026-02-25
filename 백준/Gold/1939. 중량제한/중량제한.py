import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int, input().split())

cap = [0] * (N+1)
cap[start] = 10**9

pq = [(-cap[start], start)]
ans = 0
while pq:
    cur_w, cur_node = heapq.heappop(pq)
    cur_w = (cur_w) * (-1)
    
    if cur_w < cap[cur_node]:
        continue
    
    if cur_node == end:
        ans = cur_w
        break
    
    for nxt_node, nxt_w in graph[cur_node]:
        min_w = min(cur_w, nxt_w)
        
        if min_w > cap[nxt_node]:
            cap[nxt_node] = min_w
            heapq.heappush(pq, (-min_w, nxt_node))


print(ans)