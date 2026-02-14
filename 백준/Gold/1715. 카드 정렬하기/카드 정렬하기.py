import heapq
n = int(input())
case = [int(input()) for _ in range(n)]

# 누적은 
# a+b 숫자 하나 남을때까지 반복
# 당연히 작은수끼리 먼저 더해야 함. 어차피 더하는 횟수는 동일
# 항상 가장 작은수[0] +  작은 수[1]
# n이 10^5 -> n^2 == 10^10 -> 시간 초과
# 따라서 우선순위 큐 o(log n) / o(1)

heapq.heapify(case)
ans = 0
while len(case) > 1:
    a = heapq.heappop(case)
    b = heapq.heappop(case)
    res = a+b
    ans += res
    heapq.heappush(case, res)
print(ans)