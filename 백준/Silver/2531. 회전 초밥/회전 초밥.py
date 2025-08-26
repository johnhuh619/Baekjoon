from collections import deque

N, d, k, c = map(int, input().split())
dish = []
for _ in range(N):
	dish.append(int(input()))

def sol():
    cnt = 0
    max_dish = 0

    q = deque()
    for i in range(k-1):
        q.append(dish[i])

    for j in range(N):
        q.append(dish[ (k -1 + j) % N])
        cnt = 0
        if c not in q:
            cnt = 1

        max_dish = max(max_dish, len(set(q)) + cnt)
        q.popleft()
    return max_dish

print(sol())
	

