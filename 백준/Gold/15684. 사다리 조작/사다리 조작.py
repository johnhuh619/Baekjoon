N, M, H = map(int, input().split())
line = [[0]*N for _ in range(H)]
for _ in range(M):
    x, y = map(int,input().split())
    line[x-1][y-1] = 1

def check_line():
    for i in range(N):
        temp = i
        for j in range(H):
            if line[j][temp]:
                temp += 1
            elif temp > 0 and line[j][temp -1]:
                temp -= 1
        if temp != i:
            return False
    return True

def dfs(cnt, x, y):
    """
    N은 가로줄, M은 세로줄, H는 세로줄에 놓을 수 있는 가로줄 개수
    """
    global ans
    if ans <= cnt:
        return
    if check_line():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N-1):
            if line[i][j] == 0:
                line[i][j] = 1
                dfs(cnt+1, i, j+1)
                line[i][j] = 0
                
ans = 4
dfs(0,0,0)
print(ans if ans <=3 else -1)