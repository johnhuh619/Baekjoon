from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]


for i in range(m):
    u,v  = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
q = deque([1])
visited[1] = 1
while q:
    node = q.popleft()
    for n_node in graph[node]:
        if visited[n_node] == 0:
            q.append(n_node)
            visited[n_node] = 1

print(sum(visited)-1)