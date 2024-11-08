from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start):
    num = [0]*(n+1)
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for n_node in graph[node]:
            if visited[n_node] == 0:
                num[n_node] = num[node] + 1
                visited[n_node] = 1
                q.append(n_node)
    return sum(num)
ans = []
for i in range(1, n+1):
    visited = [0]*(n+1)
    ans.append(bfs(graph,i))

print(ans.index(min(ans))+1)