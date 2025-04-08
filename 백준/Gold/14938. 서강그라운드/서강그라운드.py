import heapq

n, m, r = map(int, input().split())
val = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(r):
  s, e, v = map(int, input().split())
  graph[s-1].append((e-1,v))
  graph[e-1].append((s-1,v))

ans = 0

def dijikstra(start, graph, n):
  INF = float('inf')

  dist = [INF] * n
  dist[start] = 0

  q = [(0,start)]

  while q:
    cur_dist, cur_node = heapq.heappop(q)
    if cur_dist > dist[cur_node]:
      continue

    for n_node, w in graph[cur_node]:
      new_dist = cur_dist + w
      if new_dist < dist[n_node]:
        dist[n_node] = new_dist
        heapq.heappush(q, (new_dist, n_node))
  return dist

for i in range(n):
  dist = dijikstra(i, graph, n)
  tot = sum(val[j] for j in range(n) if dist[j] <= m)
  ans = max(ans, tot)

print(ans)