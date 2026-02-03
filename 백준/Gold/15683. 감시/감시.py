import sys

def print2D(arr):
    for i in arr:
        print(i)

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
CCTV_DIR = [
    [-1],
    [1], # 1
    [1, 3], # 2
    [0, 1], # 3
    [0, 1, 3], # 4
    [0, 1, 2, 3] # 5
]

N, M = map(int, sys.stdin.readline().split())
board = []
cctv = []
zero_cnt = 0

for row in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for col, data in enumerate(line):
        if 1 <= data <= 5:
            cctv.append((row, col, data))
        if data == 0:
            zero_cnt += 1

stk = []
result = 0

def dfs(depth):
    global result
    if depth == len(cctv):
        visit = [[False] * M for _ in range(N)]
        cnt = 0
        for idx, cctv_dirs in enumerate(stk):
            start_row, start_col, _ = cctv[idx]
            for dir in cctv_dirs:
                dx, dy = DIRS[dir]
                cur_row, cur_col = start_row, start_col
                while 0 <= cur_row < N and 0 <= cur_col < M and board[cur_row][cur_col] != 6:
                    if not visit[cur_row][cur_col] and board[cur_row][cur_col] == 0:
                        cnt += 1
                        visit[cur_row][cur_col] = True
                    cur_row += dx
                    cur_col += dy
        result = max(cnt, result)
        return
    row, col, ctype = cctv[depth]
    record_dirs = CCTV_DIR[ctype]
    if ctype == 5:
        stk.append(record_dirs)
        dfs(depth + 1)
        stk.pop()
    elif ctype == 2:
        for i in range(2):
            temp = [(record_dir + i) % 4 for record_dir in record_dirs]
            stk.append(temp)
            dfs(depth + 1)
            stk.pop()
    else:
        for i in range(4):
            temp = [(record_dir + i) % 4 for record_dir in record_dirs]
            stk.append(temp)
            dfs(depth + 1)
            stk.pop()

dfs(0)
print(zero_cnt - result)
