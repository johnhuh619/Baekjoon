from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
a = [list((map(int,input().split()))) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(K)]

ans = 987654321

for p in permutations(moves, K):
    copy_a = deepcopy(a)
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = copy_a [r-n][c+n]

            # 위, 한번에 밀기 +1
            copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n]
            
            # 우측 옆, 한번에 안되니까 아래로 한칸씩 따로 따로 밀기
            for row in range(r-n, r+n):
                copy_a[row][c-n] = copy_a[row+1][c-n]

            # 아래, 한번에 밀기 -1
            copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1]

            # 좌측 옆, 한번에 안된까 위로 한칸씩 따로 따로 밀기
            for row in range(r+n, r-n, -1):
                copy_a[row][c+n] = copy_a[row-1][c+n]

            # 안쪽 네모 처리
            copy_a[r-n+1][c+n] = tmp

    for row in copy_a:
        ans = min(ans, sum(row))

print(ans)