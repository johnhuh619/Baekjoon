N, M = map(int, input().split())
#data = sorted(list(map(int, input().split())))
data = list(range(1,N+1))
result = []
visited = [0]*N
def dfs():
    
    if len(result) == M:
        print(*result)
        return
    
    for i in range(N):
        if visited[i] == 0:
            result.append(data[i])
            visited[i] = 1
            dfs()
            result.pop()
            visited[i] = 0
dfs()