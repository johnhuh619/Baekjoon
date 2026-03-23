v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while data[idx] != -1:
        nxt = data[idx]
        cost = data[idx + 1]
        graph[node].append((nxt, cost))
        idx += 2
    

def dfs(start):
    visited = [-1] * (v+1)
    visited[start] = 0
    stack = [start]
    
    while stack:
        n = stack.pop()
        for nxt, cost in graph[n]:
            if visited[nxt] == -1:
                visited[nxt] = visited[n] + cost
                stack.append(nxt)
    
    max_node = 1
    max_dist = 0
    for i in range(1, v+1):
        if visited[i] > max_dist:
            max_dist = visited[i]
            max_node = i

    return max_node, max_dist

fn, dist = dfs(1)
mn, ans = dfs(fn)

print(ans)