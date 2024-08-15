import sys
from collections import deque, defaultdict
sys.setrecursionlimit(1000000000)
def dfs(start, graph, visited, cnt_tree):
    visited[start] = True
    cnt_tree[start] = 1

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, cnt_tree)
            cnt_tree[start]+= cnt_tree[neighbor]
    

def main():
    N, R, Q = map(int, sys.stdin.readline().split(' '))
    graph = defaultdict(list)
    visited = [False]*(N+1)
    cnt_tree = [0]*(N+1)
    data = []
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)        
        graph[v].append(u)
    for _ in range(Q):
        u = int(sys.stdin.readline().strip())
        data.append(u)

    dfs(R, graph, visited, cnt_tree)
    
    result = []
    for i in data:
        result.append(str(cnt_tree[i]))
    sys.stdout.write("\n".join(result) + "\n")

main()