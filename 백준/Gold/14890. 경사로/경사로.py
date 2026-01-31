n, l = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

# 열 검사 / 행 검사
def check(line):
    is_set = [False]*n 

    for i in range(n-1):
        diff = line[i+1] - line[i]
        if diff == 0:
            continue
        
        # up
        elif diff == 1:
            for j in range(l):
                if i - j < 0 or line[i-j] != line[i] or is_set[i-j]:
                    return False
                is_set[i-j] = True
        # down
        elif diff == -1:
            for j in range(l):
                if i+1+j >= n or line[i+1+j] != line[i+1] or is_set[i+1+j]:
                    return False
                is_set[i+1+j] = True
        else:
            return False
    return True
cnt = 0
for i in range(n):
    if check(board[i]):
        cnt += 1
for j in range(n):
    col  = [board[i][j] for i in range(n)]
    if check(col):
        cnt += 1

print(cnt)