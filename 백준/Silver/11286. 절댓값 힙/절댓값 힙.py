import heapq, sys
n = int(input())
q = []

heapq.heapify(q)

for i in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(q, (abs(num), num))
    
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)    