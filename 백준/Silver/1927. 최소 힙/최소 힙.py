import heapq
import sys
n = int(input())
hq = []
for _ in range(n):
  key = int(sys.stdin.readline().rstrip())
  if key == 0:
    if not hq:
      print(0)
    else:
      print(heapq.heappop(hq))
  else:
    heapq.heappush(hq, key)
