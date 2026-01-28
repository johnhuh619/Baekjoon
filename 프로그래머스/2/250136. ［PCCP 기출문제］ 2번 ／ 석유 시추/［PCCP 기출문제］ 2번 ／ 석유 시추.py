from collections import deque
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    ter = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    size = {}
    
    def label(sx,sy,tid):
        q = deque([(sx,sy)])
        visited[sx][sy] = True
        ter[sx][sy] = tid
        size = 1
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if land[nx][ny] == 1 and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        ter[nx][ny] = tid 
                        size += 1
        return size
            
    tid = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size[tid] = label(i,j,tid)
                tid += 1
                    
    for c in range(m):
        tot = 0
        temp = set()
        for r in range(n):
            t = ter[r][c]
            if t != 0 and t not in temp:
                temp.add(t)
                tot += size[t]    
        answer = max(answer, tot)        
    return answer