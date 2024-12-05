N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# maxDP = [[0] * 3 for _ in range(N)]
# minDP = [[0] * 3 for _ in range(N)]

maxDP_prev = [0] * 3
minDP_prev = [0] * 3

f_row = list(map(int, input().split()))
maxDP_prev[:] = f_row 
minDP_prev[:] = f_row

# 1 -> 2 start
for i in range(2,N+1):
    row = list(map(int, input().split()))
    maxDP_cur =[
        max(maxDP_prev[0], maxDP_prev[1])+row[0],
        max(maxDP_prev[0], maxDP_prev[1], maxDP_prev[2])+row[1],
        max(maxDP_prev[1], maxDP_prev[2])+row[2],
    ]
    minDP_cur = [
        min(minDP_prev[0], minDP_prev[1])+row[0],
        min(minDP_prev[0], minDP_prev[1], minDP_prev[2])+row[1],
        min(minDP_prev[1], minDP_prev[2])+row[2],
    ]
    maxDP_prev[:] = maxDP_cur
    minDP_prev[:] = minDP_cur
    
print(max(maxDP_prev), min(minDP_prev))
