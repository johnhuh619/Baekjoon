n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
stack = []
def dfs(start):
    stack.append(start) 
    visited[start] = True
    while stack:   
        cur = stack.pop()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)