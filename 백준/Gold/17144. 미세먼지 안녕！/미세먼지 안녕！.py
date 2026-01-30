r,c,t = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(r)]

top, bot = 0, 0
for i in range(r):
    if room[i][0] == -1:
        top = i
        bot = i+1
        break

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def spread():
    write_room = [[0]*c for _ in range(r)]
    write_room[top][0] = -1
    write_room[bot][0] = -1
    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                cnt = 0
                n = room[x][y] // 5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        write_room[nx][ny] += n
                        cnt += 1
                write_room[x][y] += room[x][y] - cnt* n
                
    return write_room

def airc():
    # top
    for i in range(top-1, 0, -1):
        room[i][0] = room[i-1][0]
    for j in range(c-1):
        room[0][j] = room[0][j+1]
    for i in range(top):
        room[i][c-1] = room[i+1][c-1]
    for j in range(c-1,1,-1):
        room[top][j] = room[top][j-1]
    room[top][1] = 0
    
    for i in range(bot+1,r-1):
        room[i][0] = room[i+1][0]
    for j in range(c-1):
        room[r-1][j] = room[r-1][j+1]
    for i in range(r-1,bot,-1):
        room[i][c-1] = room[i-1][c-1]
    for j in range(c-1,1,-1):
        room[bot][j] = room[bot][j-1]
    room[bot][1] = 0

for _ in range(t):
    room = spread()
    airc()
    
ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            ans += room[i][j]
print(ans)
