import heapq
n = int(input())

l = []
r = []
out = []

heapq.heapify(l)
heapq.heapify(r)

for _ in range(n):
    v = int(input())
    
    if len(l) == len(r):
        heapq.heappush(l,-v)
    else:
        heapq.heappush(r,v)
        
    
    if r and l[0] * (-1) > r[0]:
        small = heapq.heappop(r) * (-1)
        big = heapq.heappop(l) * (-1)

        heapq.heappush(l, small)
        heapq.heappush(r, big)

    out.append(str(-l[0]))

print("\n".join(out))