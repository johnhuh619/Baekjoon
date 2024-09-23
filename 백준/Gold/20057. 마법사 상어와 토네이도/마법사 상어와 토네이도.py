# 허리케인 이동 좌표
move = [(0,-1),(1,0),(0,1),(-1,0)]

# 2. 허리케인 방향에 따른 모래 비율 변경하는 함수
# array 를 반 시계방향으로 돌린다.  
def rotate_90(proportion):
    new_proportion = list(reversed(list(zip(*proportion))))
    return new_proportion

p = [
    [0, 0, 0.02, 0, 0],  # 비율 수정
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
p1 = rotate_90(p)
p2 = rotate_90(p1)
p3 = rotate_90(p2)
proportions = [ p, p1, p2, p3]
alphas = [(2,1),(3,2),(2,3),(1,2)]

# memo -> 
def solution():
    outer_sand = 0
    tr = sr
    tc = sc
    curl = 0
    turn = 2 # 좌 하단 -> 2 / 우 상단 -> 4
    now = 0
    proportion = proportions[0]
    while not (tr == 0 and tc == 0):
        tr += move[curl][0]
        tc += move[curl][1]
        now += 1                    # tornado 길이
        sand = data[tr][tc]
        data[tr][tc] = 0            # 모래 재배치 -> tornado 좌표의 모래 0
        left = sand                 # 이동하고 남은 모래

        for r in range(5):
            for c in range(5):
                now_sand = int(sand * proportion[r][c])
                left -= now_sand
                if 0 <= tr + r -2< N and 0 <= tc + c -2 < N:
                    data[tr + r - 2 ][tc + c - 2] += now_sand
                else:
                    outer_sand += now_sand
        
        if 0 <= tr + alphas[curl][0] - 2 < N and 0 <= tc + alphas[curl][1] - 2 < N:
            data[tr + alphas[curl][0] - 2][tc + alphas[curl][1] - 2] += left
        else:
            outer_sand += left
        
        if now == turn // 2 or now == turn:
            curl = (curl + 1) % 4
            proportion = proportions[curl]
            if now == turn:
                now = 0
                turn += 2

    print(outer_sand)
    return

# 1. 입력값 받기

N = int(input())
sr = sc = N//2 # 시작 좌표
data = [list(map(int,input().split())) for _ in range(N)]

solution()

