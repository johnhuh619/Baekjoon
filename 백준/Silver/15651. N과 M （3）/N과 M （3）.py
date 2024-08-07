N, M = map(int, input().split())
data = range(1,N+1)
result = []
#visited = [0]*N
def dfs():
    if len(result) == M:
        print(*result)
        return
    
    for i in range(N):
        result.append(data[i])
        dfs()
        result.pop()
dfs()
