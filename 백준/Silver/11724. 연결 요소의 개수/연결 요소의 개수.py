import sys
sys.setrecursionlimit(10**6)
n,m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
def dfs(n):
    visited[n] = True
    for node in graph[n]:
        if not visited[node]:
            dfs(node)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)