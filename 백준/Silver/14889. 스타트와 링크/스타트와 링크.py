n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
visited = [False for _ in range(n)]
res = 1e9
def dfs(man,idx):
    global res
    if man == n//2:
        # min 한지 검사
        x, y = 0,0 
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    x += board[i][j]
                elif not visited[i] and not visited[j]:
                    y += board[i][j]
        
        res = min(res,abs(x-y))
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            dfs(man+1,i+1)
            visited[i] = False
visited[0] = True            
dfs(1,1)
print(res)