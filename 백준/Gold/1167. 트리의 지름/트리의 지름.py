v = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(v):
    data = list(map(int , input().split()))
    cur = data[0]
    i = 1
    while data[i] != -1:
        node, cost = data[i], data[i+1]
        graph[cur].append((node, cost))
        i += 2
    


def dfs(start):
    stack = [start]
    visited = [-1] * (v+1)
    visited[start] = 0
    
    while stack:
        cur = stack.pop()

        for nxt, cost in graph[cur]:
            if visited[nxt] == -1:
                new_cost = cost + visited[cur]
                visited[nxt] = new_cost
                stack.append(nxt)
    
    max_node = 1
    max_dist = 0
    
    for i in range(1, v+1):
        if max_dist < visited[i]:
            max_dist = visited[i]
            max_node = i
            
    return max_node, max_dist

far_node, _ = dfs(1)
_, ans = dfs(far_node)

print(ans)

