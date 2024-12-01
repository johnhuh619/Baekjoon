R, C = map(int,input().split())
board = [list(input().strip()) for _ in range(R)]
visited = set(board[0][0])
dir = [(0,1),(1,0),(-1,0),(0,-1)]
res = 0
def dfs(x,y,cnt):
    
    global res
    res = max(res,cnt)
    
    for dx,dy in dir:
        nx, ny = x + dx, y + dy
        if 0<=nx<R and 0<=ny<C:
            if board[nx][ny] not in visited:
                visited.add(board[nx][ny])
                dfs(nx,ny,cnt+1)
                visited.remove(board[nx][ny])

    
dfs(0,0,1)
print(res)