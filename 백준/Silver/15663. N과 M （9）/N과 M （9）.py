N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []
visited = [0]*N

def dfs():
    check = 0
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if check != data[i] and visited[i] == 0:
            result.append(data[i])
            visited[i] = 1
            check = data[i]
            dfs()
            result.pop()
            visited[i] = 0

dfs()