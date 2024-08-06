N, M = map(int, input().split())
data = list(map(int, input().split()))
result = []
visited = [False] * N
data.sort()

def dfs():
    if len(result) == M:
        print(' '.join(map(str,result)))
        return
    
    for i in range(N):
        if not visited[i]:
            result.append(data[i])
            visited[i] = True
            dfs()
            visited[i] = False
            result.pop()
dfs()