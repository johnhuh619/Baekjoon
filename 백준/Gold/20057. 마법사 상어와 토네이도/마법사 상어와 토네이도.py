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
        sand = data[tr][tc]         # 재분배할 모래 양 저장
        data[tr][tc] = 0            # 모래 재배치 -> tornado 좌표의 모래 0 (전부 이동할 거니까 zero)
        left = sand                 # 이동하고 남은 모래 -> a 알파로 이동함

        for r in range(5):                  
            for c in range(5):
                now_sand = int(sand * proportion[r][c])         # 현재 모래 비율 값 가져오기 + 모래 곱하기 = 현재 모래 (모래 재분배 과정)
                left -= now_sand                                # left에서 현재 칸의 모래를 빼준다. (계속 이동시키는 중이니까.)
                if 0 <= tr + r -2< N and 0 <= tc + c -2 < N:    # 격자 외곽으로 날아갔는지 검사. 아니라면, 현재 검사한 칸에 모래 양을 반영해준다.
                    data[tr + r - 2 ][tc + c - 2] += now_sand   
                else:
                    outer_sand += now_sand # 격자 외곽이라면, (칸마다 검사하는 중임) now sand 를 outer_sand 에 저장해준다. 외곽으로 날라간 모래니까.
        
        if 0 <= tr + alphas[curl][0] - 2 < N and 0 <= tc + alphas[curl][1] - 2 < N: # 알파가 격자 안인지 검사
            data[tr + alphas[curl][0] - 2][tc + alphas[curl][1] - 2] += left        # 안이면 값을 넣어준다. 알파 = left 된 모래 니까
        else:
            outer_sand += left                                                      # 알파의 위치가 격자 밖이라면, outer_sand에 저장해준다.
        
        # 토네이도는 같은 거리를 두 번 이동하고 방향을 바꾸며, 이동 거리는 두 번의 방향 전환 후에 증가한다.
        # 첫 번째 방향 전환은 now == turn // 2일 때 발생한다.
        # 두 번째 방향 전환은 now == turn일 때 발생하며, 이때 이동 거리를 늘려야 하므로 turn을 증가시킨다

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

