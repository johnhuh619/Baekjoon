from collections import deque, defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)
    
    for s in graph:
        graph[s].sort(reverse=True)
        
    stack = deque(["ICN"])
    route = []
    
    while stack:
        cur = stack[-1]
        if not graph[cur]:
            route.append(stack.pop())
        else:
            stack.append(graph[cur].pop())
    return route[::-1]
            