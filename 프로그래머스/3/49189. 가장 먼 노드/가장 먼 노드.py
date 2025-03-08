from collections import deque

def solution(n, edge):
    answer = 0
    # 최단 경로
    # 간선의 가중치가 동일 => unweighted graph 이다
    # 따라서 dijkstra를 쓰지 않아도 된다
    graph = [[] for _ in range(n+1)]
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    q = deque([1])
    distances = [-1]*(n+1)
    distances[1] = 0
    while q:
        node = q.popleft()
        for n in graph[node]:
            if distances[n] == -1:
                distances[n] = distances[node] + 1
                q.append(n)
    max_dis = max(distances)        
    return distances.count(max_dis)