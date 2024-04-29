import sys
from collections import deque


# 1. 스티커를 회전시켜서
# 2. 공간에 들어가는지 확인한다
# ...


# 먼저 스티커를 90도 돌리는 함수
def rotate(origin):
    # new_c => 원래 row
    # new_r => 원래 col
    new_r = len(origin[0])
    new_c = len(origin)
    new_sticker = [[0 for _ in range(new_c)] for i in range(new_r)]

    que = deque()
    for i in range(new_c):
        for j in range(new_r):
            que.append(origin[i][j])

    for j in range(new_c - 1, -1, -1):
        for i in range(new_r):
            new_sticker[i][j] = que.popleft()

    return new_sticker


# 현재 위치에서 스티커를 붙일 수 있는가 T/F 여부 확인 하는 함수
def check_stick_on_board(r_start, c_start, now_sticker):
    global board
    stick_row_idx = 0
    for r in range(r_start, r_start + len(now_sticker)):
        stick_col_idx = 0
        for c in range(c_start, c_start + len(now_sticker[0])):
            if r < 0 or c < 0 or r >= N or c >= M:
                return False
            if now_sticker[stick_row_idx][stick_col_idx] == 1 and board[r][c] == 1:
                return False
            stick_col_idx += 1
        stick_row_idx += 1
    return True


# 보드에서 스티커를 붙일 위치를 탐색
def find_position(now_sticker):
    global board
    for r_start in range(N):
        for c_start in range(M):
            result = check_stick_on_board(r_start, c_start, now_sticker)
            if result:
                return True, r_start, c_start
    return False, -1, -1


N, M, K = map(int, sys.stdin.readline().rstrip().split())
# 보드의 default 상태 N열 M행.
board = [[0 for _ in range(M)] for _ in range(N)]

# 1. 붙여야 하는 스티커를 순서대로 받는다
# 2. 스티커를 붙일 수 있는 곳에 붙인다
# 스티커 개수 = K개
for p in range(1, K + 1):
    # 스티커 크기 입력 받는다.
    R, C = map(int, sys.stdin.readline().rstrip().split())
    # 스티커 모양을 입력 받는다.
    sticker = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(R)]

    # 스티커를 붙인다
    # 각도 4종류 => 4회
    for _ in range(4):
        # 보드에서 붙일 위치 탐색
        can_stick = find_position(sticker)

        if can_stick[0]:
            stick_r_idx = 0
            for i in range(can_stick[1], can_stick[1] + len(sticker)):
                stick_c_idx = 0
                for j in range(can_stick[2], can_stick[2] + len(sticker[0])):
                    # 스티커를 보드에 붙인다 (보드의 "0" => "1")
                    if sticker[stick_r_idx][stick_c_idx] == 1:
                        board[i][j] = sticker[stick_r_idx][stick_c_idx]
                    stick_c_idx += 1
                stick_r_idx += 1
            break
        else:
            sticker = rotate(sticker)

# 다 붙이면 1이 몇개 인지 센다
answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            answer += 1
print(answer)