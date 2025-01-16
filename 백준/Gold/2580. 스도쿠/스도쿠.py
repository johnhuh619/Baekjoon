
# 9 상수
SIZE = 9

array = [list(map(int,input().split())) for _ in range(SIZE)]
# 0 위치 좌표
blank = [(i,j) for i in range(SIZE) for j in range(SIZE) if array[i][j] == 0]

def check(y, x, check_num):
    BOX_SIZE = 3
    for i in range(SIZE):
        if check_num == array[i][x] or check_num == array[y][i]:
            return False
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if array[y // BOX_SIZE * BOX_SIZE + i][x // BOX_SIZE * BOX_SIZE + j] == check_num:
                return False
    return True


def dfs(n):
    if n == len(blank):
        for i in array:
            print(*i)
        exit()
        
    for check_num in range(1,10):
        y, x = blank[n]
        
        if check(y, x, check_num):
            array[y][x] = check_num
            dfs(n+1)
            array[y][x] = 0

    
dfs(0)