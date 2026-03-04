n, m = map(int, input().split())
w = [list(map(int,input().split())) for _ in range(n)]
sx, sy, pipes = map(int, input().split())

ans = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False]*m for _ in range(n)]
def dfs(x, y, cnt, prev_dir, tot):
    global ans    

    ans = max(ans, tot)
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            cost = 1
            if prev_dir != -1 and prev_dir != d:
                cost += 1
                
            if cnt + cost > pipes:
                continue
            
            visited[nx][ny] = True
            dfs(nx, ny, cnt + cost, d, tot + w[nx][ny])
            visited[nx][ny] = False

visited[sx][sy] = True
dfs(sx, sy, 0, -1, w[sx][sy])
print(ans)
