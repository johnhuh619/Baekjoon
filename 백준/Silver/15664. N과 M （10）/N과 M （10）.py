N, M = map(int, input().split())
data = sorted(map(int, input().split()))
result = []
visited =[0]*N

def dfs(start):
    if len(result) == M:
        print(*result)
        return
    check = 0
    for i in range(start,N):
        if check != data[i] and visited[i] == 0:
            check = data[i]
            result.append(data[i])
            visited[i] = 1
            dfs(i+1)
            visited[i] = 0
            result.pop()

dfs(0)
