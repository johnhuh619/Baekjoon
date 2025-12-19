
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 0
def dfs(x, y, depth, tot):
    global ans
    
    if depth == 4:
        ans = max(ans, tot)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, tot + graph[nx][ny])
            visited[nx][ny] = False

def check_ex(x, y):
    global ans
    vals = []
    center = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            vals.append(graph[nx][ny])
    
    if len(vals) >= 3:
        ans = max(ans, center + sum(vals) - (min(vals) if len(vals) == 4 else 0))

for i in range(n):
    for j in range(m):
        # 연속된 모양 처리
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False

        # T 자 처리
        check_ex(i,j)

print(ans)