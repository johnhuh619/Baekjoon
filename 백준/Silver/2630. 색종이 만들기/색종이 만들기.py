import sys
def div(y,x,n):
    # 초기 색 좌표 넘겨주는듯?
    color = paper[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if color != paper[i][j]:
                new_n = n//2
                div(y,x,new_n)              # 1            
                div(y,x+new_n,new_n)        # 2
                div(y+new_n,x+new_n,new_n)  # 3
                div(y+new_n,x,new_n)        # 4
                return
    if color == 0:
        res[0] += 1
    else:
        res[1] += 1
    



n = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
res = [0,0]
div(0,0,n)
print(res[0], '\n', res[1], sep='')