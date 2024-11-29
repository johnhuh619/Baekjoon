N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)    

visited = [False]*N
cnt = 0
def dfs(c_node,depth):

    global cnt
    
    if cnt:
        return
    
    if depth == 4:
        cnt = 1
        return
    
    visited[c_node] = True
    for n_node in graph[c_node]:
        if not visited[n_node]:
            dfs(n_node, depth+1)
    visited[c_node] = False

for i in range(N):
    dfs(i,0)
    if cnt:
        break

print(cnt)            
            