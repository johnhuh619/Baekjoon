from collections import defaultdict, deque
import sys
def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    node_cnt = 0
    edge_cnt = 0

    while queue:
        node = queue.popleft()
        node_cnt += 1
        for neighbor in graph[node]:
            edge_cnt += 1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    edge_cnt //= 2
    
    return node_cnt -1 == edge_cnt


def count_trees(n, edges):
    if n == 0:
        return 0
    
    graph = defaultdict(list)
    visited = [False]*(n+1)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    tree_cnt = 0

    for node in range(1,n+1):
        if not visited[node]:
            if bfs(node, graph, visited):
                tree_cnt += 1
    
    return tree_cnt

def main():
    case_num=1
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        edges = []
        for _ in range(m):
            u, v = map(int, input().split())
            edges.append((u,v))
        
        tree_count = count_trees(n,edges)
        if tree_count == 0:
            print(f"Case {case_num}: No trees.")
        elif tree_count == 1:
            print(f"Case {case_num}: There is one tree.")
        else:
            print(f"Case {case_num}: A forest of {tree_count} trees.")
        
        case_num += 1

main()
