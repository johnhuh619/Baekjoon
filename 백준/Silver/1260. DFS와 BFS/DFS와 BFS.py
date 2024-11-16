from collections import deque
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
for i in range(1,n+1):
    graph[i].sort()

def bfs(start):
    visited = [0]*(n+1)
    q = deque([start])
    visited[start] = 1
    while q:
        node = q.popleft()
        print(node, end=' ')
        for n_node in graph[node]:
            if not visited[n_node]:
                visited[n_node] = 1
                q.append(n_node)

visited = [0]*(n+1)
def dfs(c_node,visited):
    visited[c_node] = 1
    print(c_node,end=' ')
    for n_node in graph[c_node]:
        if not visited[n_node]:
            dfs(n_node,visited)

dfs(v,visited)
print()
bfs(v)


    