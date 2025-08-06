import heapq
import sys

n, m, r = map(int,input().split())
val = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
  v1, v2, w = map(int, input().split())
  graph[v1].append((v2,w))
  graph[v2].append((v1,w))

INF = sys.maxsize

def djikstra(start):
  dist = [INF]*(n+1)
  dist[start] = 0
  hq = [(0,start)]

  while hq:
    tot_dist, cv = heapq.heappop(hq)
    if tot_dist > dist[cv]:
      continue

    for nv, n_dist in graph[cv]:
      new_dist = tot_dist + n_dist
      if new_dist < dist[nv]:
        dist[nv] = new_dist
        heapq.heappush(hq, (new_dist, nv))
  return dist

ans = 0

for i in range(1,n+1):
  dist = djikstra(i)
  tot = 0
  for j in range(1, n+1):
    if dist[j] <= m:
      tot += val[j-1]
  ans = max(ans, tot)
print(ans)