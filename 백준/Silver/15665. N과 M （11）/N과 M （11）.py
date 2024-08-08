N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
result =[]
visited = [0]*N

def dfs():
    if len(result) == M:
        print(*result)
        return
    check = 0    
    for i in range(N):
        if check != data[i]:
            result.append(data[i])
            check = data[i]
            visited[i] = 1
            dfs()
            visited[i] = 0
            result.pop()

dfs()