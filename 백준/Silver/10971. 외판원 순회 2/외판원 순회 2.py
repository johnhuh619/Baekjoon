N = int(input())
w = [list(map(int, input().split())) for _ in range(N)]

def dfs(s, e, totw, visited):
    
    if False not in visited:
        if w[s][e] > 0:
            return totw + w[s][e]        
        
    min_cost = float('inf')
    
    for i in range(N):
        if not visited[i] and w[s][i] > 0:
            visited[i] = True
            min_cost = min(min_cost, dfs(i, e, totw + w[s][i], visited))
            visited[i] = False
    return min_cost

visited = [False]*N
visited[0] = True
res = dfs(0,0,0,visited)

print(res)