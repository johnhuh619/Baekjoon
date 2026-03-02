n, m = map(int, input().split())
w = [list(map(int, input().split())) for _ in range(n)]    
sx, sy, p = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[False]*m for _ in range(n)]
visited[sx][sy] = True

start = w[sx][sy]
ans = start

def dfs(x, y, prev_dir, cnt, cur_sum):
    global ans
    
    ans = max(ans, cur_sum)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            point = 1
            if prev_dir != -1 and i != prev_dir:
                point += 1 # ㄱ 자 파이프로 교체
            
            # cost
            if cnt + point > p:
                continue
            
            visited[nx][ny] = True
            dfs(nx, ny, i, cnt + point, cur_sum + w[nx][ny])
            visited[nx][ny] = False

for d in range(4):
    nx = sx + dx[d]
    ny = sy + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        if p >= 1:
            visited[nx][ny] = True
            dfs(nx, ny, d, 1, start + w[nx][ny])
            visited[nx][ny] = False
            
    
print(ans)