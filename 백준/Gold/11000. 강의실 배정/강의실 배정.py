import heapq
n = int(input())
time = []
for i in range(n):
  s, t = map(int, input().split())
  time.append((s,t))

time.sort(key=lambda x: x[0])

pq= []
max_rooms = 0

for s,e in time:
  if pq and pq[0] <= s:
    heapq.heappop(pq)
  
  heapq.heappush(pq,e)
  max_rooms = max(max_rooms, len(pq))

print(max_rooms)