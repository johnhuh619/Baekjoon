import math

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] =a
    else:
        parent[a] = b
    

N, M = map(int, input().split())
parent = [i for i in range(N)]
graph = []
for _ in range(N):
    x, y = map(int, input().split())
    graph.append((x,y))
    
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 좌표 인덱스는 0부터 시작
    b -= 1
    union_parent(parent, a, b)
answer = 0

# 간선 가중치 계산 + 정렬
edges = []
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = graph[i]
        x2, y2 = graph[j]
        cost = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        edges.append((cost, i, j))
    
edges.sort()    # cost 로 정렬

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(f'{answer:.2f}')
