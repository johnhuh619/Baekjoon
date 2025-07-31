import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  start, end, val = map(int, input().split())
  graph[start].append((end,val))

start, end = map(int, input().split())
# 해당 노드까지의 최단비용 합
costs = [(1e9) for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap,[0,start])
while heap:
  c_value, c_node = heapq.heappop(heap)
  if costs[c_node] < c_value:
    continue
  for n_node, n_value in graph[c_node]:
    sum_v = c_value + n_value
    if sum_v >= costs[n_node]:
      continue
    costs[n_node] = sum_v
    heapq.heappush(heap,[sum_v, n_node])

print(costs[end])
               