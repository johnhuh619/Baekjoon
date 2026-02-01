n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

house = []
chick = []
sel_chick = []
min_dist = float('inf')

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i,j))

        elif board[i][j] == 2:
            chick.append((i,j))

h = len(house)
c = len(chick)

dist = [[0]*c for _ in range(h)]
for i, (hr, hc) in enumerate(house):
    for j, (cr, cc) in enumerate(chick):
        dist[i][j] = abs(hr-cr) + abs(hc-cc)

             
    
def dfs(idx, cnt):
    global min_dist
    
    if cnt == m:
        tot_dist = 0
        for ho in range(h):
            best = float('inf')
            for ch in sel_chick:
                best = min(best, dist[ho][ch])
            tot_dist += best

            if tot_dist >= min_dist:
                return
        min_dist = tot_dist
        return
    
    for i in range(idx, c):
        sel_chick.append(i)
        dfs(i+1, cnt+1)
        sel_chick.pop()

dfs(0,0)
print(min_dist)
