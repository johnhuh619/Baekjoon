from collections import deque
# n = node 개수
# computers = 노드 모음집
def solution(n, computers):
    
    visited = [False] * n
    def dfs(start):
        stack = deque([start])
        while stack:
            cur = stack.pop()            
            for i in range(len(computers[cur])):
                if computers[cur][i] == 1 and not visited[i]:
                    stack.append(i)
                    visited[i] = True
    
    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    return cnt