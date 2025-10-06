import copy
def rotate90(matrix):
    M = len(matrix)
    rotated = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotated[j][M-1-i] = matrix[i][j]
    return rotated

def create_extend_board(lock, M):
    N = len(lock)
    size = N + 2*(M-1)
    new_board = [[0]*(size) for _ in range(size)]
    for i in range(N):
        for j in range(N):
            new_board[i + M -1][j + M -1] = lock[i][j]
    return new_board

def check(board, key, x, y, M, N):
    b = copy.deepcopy(board)
    for i in range(M):
        for j in range(M):
            b[x + i][y + j] += key[i][j]
    
    for i in range(N):
        for j in range(N):
            if b[i + M - 1][j + M - 1] != 1:
                return False
    return True
              
    
    
    
def solution(key, lock):
    answer = True
    # 1. 확장 보드 생성
    M = len(key)
    N = len(lock)
    board = create_extend_board(lock, M)
    size = len(board)
    k = key
    
    # for loop (회전: 0, 90, 180, 270)
    for r in range(4):
        #   for loop (x,y)
        for i in range(size - M + 1):
            for j in range(size - M + 1):
                #       2. 확장 보드 복사
                #       3. x, y 위치에 열쇠 부착
                #       4. 영역 검증
                if check(board, k, i, j, M, N):
                    return True
        k = rotate90(k)
    # 이동 시키면서 가능한 위치 찾기
    # 찾는 순간 for loop 종료 / return True
    return False