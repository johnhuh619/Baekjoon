from collections import deque
n = int(input())
q = deque()
for i in range(n):
    q.append(i+1)

while len(q) != 1:
    q.popleft()
    if len(q) == 1:
        continue
    a = q.popleft()
    q.append(a)

print(q[0])