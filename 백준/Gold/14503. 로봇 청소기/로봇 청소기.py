N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for i in range(N):
    room.append(list(map(int, input().split())))

cnt = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    
    found = False        
    
    for _ in range(4):
        d = (d + 3)% 4
        nx = r + dx[d]
        ny = c + dy[d]
        if room[nx][ny] == 0:
                r, c = nx, ny
                found = True        
                break
            
    if not found:
        back = (d + 2) % 4
        bx = r + dx[back]
        by = c + dy[back]
        if room[bx][by] == 1:
            break
        else:
            r, c = bx, by


print(cnt)