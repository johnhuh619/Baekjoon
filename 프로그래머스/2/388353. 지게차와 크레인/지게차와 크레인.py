from collections import deque
def solution(storage, requests):
    answer = 0
    # air: 0, non: 1
    n = len(storage) 
    m = len(storage[0])
    field = [[0] * (m+2) for _ in range(n+2)]
    
    for i in range(n):
        for j in range(m):
            field[i+1][j+1] = storage[i][j]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def bfs(target):
        delist = []
        visited = [[False]*(m+2) for _ in range(n+2)]
        q = deque([(0,0)])           
        visited[0][0] = True
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n + 2 and 0 <= ny < m +2 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if field[nx][ny] == 0:
                        q.append((nx,ny))
                    elif field[nx][ny] == target:
                        field[nx][ny] = 0
                
    def crane(target):
        for i in range(1,n+1):
            for j in range(1,m+1):
                if field[i][j] == target:
                    field[i][j] = 0
                    
    for rq in requests:
        if len(rq) == 1:
            bfs(rq)
        else:
            crane(rq[0])
            
    for i in range(1, n+1):
        for j in range(1, m+1):
            if field[i][j] != 0:
                answer += 1
                
    return answer