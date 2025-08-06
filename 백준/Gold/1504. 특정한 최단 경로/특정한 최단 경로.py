import heapq
import sys

n, e = map(int, input().split())
graph = [ [] for _ in range(n+1)]

for _ in range(e):
  v1, v2, w = map(int, input().split())
  graph[v1].append((v2, w))
  graph[v2].append((v1, w))

v1, v2 = map(int, input().split())

# 1 -> v1 -> v2 -> end
# 1 -> v2 -> v1 -> end

INF = sys.maxsize

def djikstra(start):
  pq = [(0, start)]
  route = [INF] * (n+1)
  route[start] = 0

  while pq:
    tot_w, cur_v = heapq.heappop(pq)
    if tot_w > route[cur_v]:
      continue

    for nv, nw in graph[cur_v]:
      new_dist = tot_w + nw
      if new_dist < route[nv]:
        route[nv] = new_dist
        heapq.heappush(pq, (new_dist, nv))

  return route

dist_from_1 = djikstra(1)
dist_from_v1 = djikstra(v1)
dist_from_v2 = djikstra(v2)

r1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
r2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

if r1 >= INF and r2 >= INF:
  print(-1)
else:
  print(min(r1, r2))