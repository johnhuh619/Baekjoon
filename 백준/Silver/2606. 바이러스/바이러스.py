from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited=[0]*(n+1)

for i in range(m):
    a ,b = map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]

visited[1]=1
q=deque([1])
while q:
    c = q.popleft()
    for k in graph[c]:
        if visited[k] == 0:
            q.append(k)
            visited[k] = 1  

print(sum(visited)-1)