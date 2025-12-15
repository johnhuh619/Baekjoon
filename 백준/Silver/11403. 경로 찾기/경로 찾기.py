import sys

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 1:
            graph[i].append(j)
res = [[0]*n for _ in range(n)]

def dfs(start):
    visited = [0] * n
    stack = [start]
    
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                stack.append(nxt)

    return visited

for i in range(n):
    visited = dfs(i)
    for j in range(n):
        res[i][j] = visited[j]

for row in res:
    print(*row)

            

                
            
    
    

        