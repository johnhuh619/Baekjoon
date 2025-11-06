from collections import defaultdict, deque    
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    def bfs(start, cut):
        visited = set()
        q = deque([start])
        visited.add(start)
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                if nxt in cut and node in cut:
                    continue
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return len(visited)
    
    cur = n
    for s, e in wires:
        cnt = bfs(s, (s,e))
        dif = abs(n- 2*cnt)
        cur = min(cur,dif)
    return cur