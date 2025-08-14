def solution(n, computers):
    
    visited = [False] * n
    cnt = 0

    for i in range(n):
        if not visited[i]:
            stack = [i]

            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for j in range(n):
                        if computers[node][j] == 1 and not visited[j]:
                            stack.append(j)
            
            cnt += 1
    return cnt