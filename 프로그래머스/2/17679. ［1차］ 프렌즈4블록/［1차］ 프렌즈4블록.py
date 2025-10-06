from collections import deque
def simulator(m, n, board):
    lst = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == '0':
                continue
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                lst.add((i,j))
                lst.add((i,j+1))
                lst.add((i+1,j))
                lst.add((i+1,j+1))
    return lst

def remove_blocks(board, to_remove):
    for i, j in to_remove:
        board[i][j] = '0'
        
def drop_blocks(m,n,board):
    for j in range(n):
        blocks = deque()
        for i in range(m-1, -1, -1):
            if board[i][j] != '0':
                blocks.append(board[i][j])
        
        for i in range(m-1, -1, -1):
            if blocks:
                board[i][j] = blocks.popleft()
            else:
                board[i][j] = '0'
    
def solution(m, n, board):
    board = [list(r) for r in board]
    
    answer = 0
    while True:
        to_remove = simulator(m,n,board)
        if not to_remove:
            break
        answer += len(to_remove)
        remove_blocks(board, to_remove)
        drop_blocks(m, n, board)

    return answer
