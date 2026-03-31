import heapq
n = int(input())
m = int(input())

nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    nodes[a].append((b, c))
    
start, end = map(int, input().split())
INF = int(1e9)
dist = [INF] * (n+1)
prev = [[] for _ in range(n+1)]

def djikstra(s):
    pq = [(0, s)]
    dist[s] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        
        if dist[node] < cost:
            continue
        
        for nxt, nc in nodes[node]:
            new_cost = nc + dist[node]
            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                prev[nxt] = node
                heapq.heappush(pq, (new_cost, nxt))
        

djikstra(start)
path = []
cur = end
while cur:
    path.append(cur)
    cur = prev[cur]

path.reverse()     
print(dist[end])
print(len(path))
print(*path)
