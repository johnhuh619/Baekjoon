import heapq
n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)
for _ in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    temp = a+b
    heapq.heappush(cards, temp)
    heapq.heappush(cards, temp)

print (sum(cards))
    
    