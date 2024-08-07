N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []

def dfs(start):
    check = 0
    if len(result) == M:
        print(*result) 
        return
    
    for i in range(start, N):   
        if check != data[i]:
            result.append(data[i])
            check = data[i]
            dfs(i)
            result.pop()



dfs(0)