import heapq

n = int(input())
lecture = []
for _ in range(n):
    num, start, end = map(int,input().split())
    lecture.append((start, end))

lecture.sort()
pq = []

heapq.heappush(pq,lecture[0][1])

for i in range(1,n):
    start, end = lecture[i]
    if pq[0] <= start:
        heapq.heappop(pq)
    
    heapq.heappush(pq,end)

print(len(pq))        
