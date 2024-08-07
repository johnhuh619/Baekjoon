N, M = map(int, input().split())
data = sorted(list(map(int,input().split())))
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return

    for i in range(N):
        result.append(data[i])
        dfs()
        result.pop()
dfs()