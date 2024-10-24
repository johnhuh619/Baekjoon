from collections import deque, defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for s,e in tickets:
        graph[s].append(e)
    for s in graph:
        graph[s].sort(reverse=True)
    stack = deque(["ICN"])
    route = []
    while stack:
        current = stack[-1]    # 맨 위
        if not graph[current]: # 방문 안했으면, route에 추가.
            route.append(stack.pop())
        else:
            stack.append(graph[current].pop()) # 방문 했으면, pop
    return route[::-1]