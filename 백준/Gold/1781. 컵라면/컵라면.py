import heapq

n = int(input())
cups = []
for _ in range(n):
    a, b = map(int, input().split())
    cups.append((a,b))

cups.sort()

pq = []
heapq.heapify(pq)

for dead, value in cups:
    heapq.heappush(pq, value)
    if len(pq) > dead:  
        heapq.heappop(pq)

print(sum(pq))