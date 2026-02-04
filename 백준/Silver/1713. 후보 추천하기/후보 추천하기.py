n = int(input())
tot = int(input())
recommend = list(map(int,input().split()))

board = {}
len_board = 0
for time, p in enumerate(recommend):
    
    if p in board:
       board[p][0] += 1
    
    elif len(board) < n:
        board[p] = [1, time]

    else:
        remove = min(
            board.items(),
            key = lambda x: (x[1][0], x[1][0]) # 추천/ 시간
        )[0]
    
        del board[remove]
        board[p] = [1, time]
        
print(' '.join(map(str,sorted(board.keys()))))