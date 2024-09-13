N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]

dy8 = ("empty", 0, -1, -1, -1, 0 , 1, 1, 1)
dx8 = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)

dy4 = (-1, -1, 1, 1)
dx4 = (-1, 1, -1, 1)

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] # 구름 좌표

for d, s in moves:
    moved_clouds = []
    # 비바라기 사용
    for y, x in clouds:
        # d 방향으로 s만큼 이동
        ny = (y + dy8[d] * s) % N
        nx = (x + dx8[d] * s) % N
        matrix[ny][nx] += 1 # 물의 양 추가
        moved_clouds.append((ny, nx)) # 이동한 구름 좌표에 추가
    # 물복사 버그 사용
    for y, x in moved_clouds:
        # 이동한 구름들의 대각 4방향을 조사하여 cnt 만큼의 물의 양 추가
        cnt = 0 
        for d in range(4):
            ny = y + dy4[d]
            nx = x + dx4[d]
            if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] > 0:
                cnt += 1
        matrix[y][x] += cnt

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    # 이때 구름이 생기는 칸은 구름이 사라진 칸이 아니어야 한다.
    new_clouds = []
    for y in range(N):
        for x in range(N):
            if (y, x) not in moved_clouds and matrix[y][x] >= 2:
                matrix[y][x] -= 2        
        # 물 -= 2  && 새로운 구름 배열 추가
                new_clouds.append((y,x))
    clouds = new_clouds
result = 0
for y in range(N):  
    for x in range(N):
        result += matrix[y][x]
print(result)

