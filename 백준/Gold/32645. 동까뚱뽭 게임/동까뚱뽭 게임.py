import sys
sys.setrecursionlimit(200000)

def dfs(cur, parent, tree, depth):
    check = False
    for next in tree[cur]:
        if next == parent: 
            continue
        if not dfs(next, cur, tree, depth):  # 자식 노드가 혁준 승리라면
            check = True
    depth[cur] = check
    return check

n = int(input().strip())
tree = [[] for _ in range(n + 1)]
depth = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS 시작
start = 1
dfs(start, start, tree, depth)

# 각 노드의 승패 출력
for i in range(1, n + 1):
    if depth[i]: 
        print("donggggas")  # 동우 승리
    else:
        print("uppercut")  # 혁준 승리

