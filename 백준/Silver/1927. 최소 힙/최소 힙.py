import heapq
import sys
n = int(input())
h = []
for _ in range(n):
    key = int(sys.stdin.readline().rstrip())
    if key == 0:
        try:
            print(heapq.heappop(h))
        except:
            print(0)
    else:
        heapq.heappush(h,key)   