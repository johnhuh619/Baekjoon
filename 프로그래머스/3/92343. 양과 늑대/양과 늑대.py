from collections import deque
def solution(info, edges):
    ans = 0
    graph = [[] for _ in range(len(info))]
    for e in edges:
        graph[e[0]].append(e[1])
        
    stack = deque([(1, 0, set(graph[0]))])
        
    while stack:
        cs, cw, cc = stack.pop()
        ans = max(ans, cs)
        
        for nxt in cc:
            nc = cc.copy()
            nc.remove(nxt)
            nc.update(graph[nxt])
        
            if info[nxt] == 0:
                stack.append((cs+1, cw, nc))
            
            else:
                if cs > cw+1:
                    stack.append((cs, cw+1, nc))
            
    return ans