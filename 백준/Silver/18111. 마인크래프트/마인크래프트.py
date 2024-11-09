import sys
n, m, b =  map(int,input().split())
graph = []
idx = 0
ans = float('inf')
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    

for floor in range(257):
    min_b, max_b = 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= floor:
                max_b += graph[i][j] - floor
            else:
                min_b += floor - graph[i][j]
    if (max_b+b) >= min_b:
        if max_b*2 + min_b <= ans:
            ans = max_b*2 + min_b
            idx = floor
    
print(ans, idx)