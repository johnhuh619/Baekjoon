N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []
visited = [0]*N
def dfs(start):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(start,N):
        if visited[i] == 0:
            result.append(data[i])
            visited[i] = 1
            dfs(i+1)
            visited[i] = 0
            result.pop()

dfs(0)


