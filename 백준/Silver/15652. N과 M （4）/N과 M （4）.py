N, M = map(int, input().split())
data = range(1,N+1)
result = []
def dfs(start):
    if len(result) == M:
        print(*result)
        return
    for i in range(start,N):
        result.append(data[i])
        dfs(i)
        result.pop()

dfs(0)
