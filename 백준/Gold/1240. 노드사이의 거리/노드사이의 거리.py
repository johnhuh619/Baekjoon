import sys


def dfs(start, end, check):
    global count
    
    if start == end:
        count = check
        return
    
    for node, weight in Tree[start]:
        if not visit[node]:
            visit[node] = True
            dfs(node, end, check + weight)

def main():
    global count, Tree, visit

    N, M = map(int, input().split())
    Tree = [[] for _ in range(N+1)]
    for i in range(N-1):
        u, v, w = map(int, input().split())
        Tree[u].append([v,w])
        Tree[v].append([u,w])
    for _ in range(M):
        u, v = map(int, input().split())
        visit = [False]*(N+1)
        count = 0
        visit[u] = True
        dfs(u,v,0)
        print(count)

main()