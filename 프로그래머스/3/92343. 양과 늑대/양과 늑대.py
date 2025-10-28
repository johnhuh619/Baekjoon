from collections import deque
def solution(info, edges):
    # wolf, sheep
    # 전공
    # lv.2
    ans = 0
    graph = [[] for _ in range(len(info))]
    
    for s, e in edges:
        graph[s].append(e)
    
    # s, w, visited
    stack = deque([(1, 0, set(graph[0]))])
    max_sheep = 0
    while stack:
        cs, cw, can = stack.pop()
        max_sheep = max(max_sheep, cs)
        
        # [[2,3],[4,5],[6,7]]
        # [2,3]
        # [3,4,5] / [2,6,7]
        for nxt in can:
            n_can = can.copy()
            n_can.remove(nxt)
            n_can.update(graph[nxt])
            
            if info[nxt] == 0:
                stack.append((cs+1, cw, n_can))
            else:
                if cs > cw+1:
                    stack.append((cs, cw+1, n_can))
            
    return max_sheep