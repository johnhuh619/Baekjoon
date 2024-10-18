from collections import deque
board = [list(input()) for _ in range(5)]
idx = [(i,j) for i in range(5) for j in range(5)]
s = [] # 7공주 뽑은 조합. 7개
n = [] # 
ans = 0
def is_available(s):
    l = [i for i in s]  # s에 대한 사실상 shallow copy (조합 7개가 담겨 있음)
    dir = [(1,0),(-1,0),(0,-1),(0,1)]
    q = deque()
    
    q.append(l[0])
    l.remove(l[0])  # 0번째 위치좌표 로 시작 
    while q:
        x,y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if (nx,ny) in l:
                q.append((nx,ny))
                l.remove(((nx,ny)))
    if len(l) == 0:
        return True
    return False


# S 파 > Y 파
# 5 x 5 에서 중복 없이 7개 뽑는 경우의 수가 필요
def dfs(depth):
    global ans
    if len(s) == 7:
        if n.count('S') >= 4 and is_available(s):
            ans += 1
        return
    for i in range(depth, 25):
        x, y = idx[i]
        s.append((x,y)) 
        n.append(board[x][y])
        dfs(i+1)
        s.pop()
        n.pop()

        
dfs(0)
print(ans)