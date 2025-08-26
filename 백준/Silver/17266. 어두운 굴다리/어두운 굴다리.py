N = int(input())
M = int(input())
p = list(map(int, input().split())) # 좌표


h = p[0]
h = max(h, N-p[-1])
cur = p[0]
for i in range(1, len(p)):
	tmp = p[i] - p[i-1]
	dist = (tmp+1)//2
	h = max(h, dist)

print(h)


