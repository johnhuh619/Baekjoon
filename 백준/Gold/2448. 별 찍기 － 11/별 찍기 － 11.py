
def star(n):
    board = [[' ' for _ in range(2*n -1)] for _ in range(n)]
    
    def recursive_star(x,y,size):
        # 기본 삼각형
        if size == 3:
            board[x][y] = "*"
            board[x+1][y-1] = "*"
            board[x+1][y+1] = "*"
            # board[x+2][y-2:y+3] = ["*","*","*","*","*"]
            for k in range(-2, 3):
                board[x+2][y+k] = "*"
            return board
        
        mid = size//2
        # 위
        recursive_star(x,y,mid)
        # 좌
        recursive_star(x+mid,y-mid,mid)
        # 우
        recursive_star(x+mid,y+mid,mid)
    
    recursive_star(0,n-1,n)
    return board


res = star(int(input()))

for result in res:
    print("".join(result))