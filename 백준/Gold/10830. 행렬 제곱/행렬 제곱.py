import sys

def sol():
    N, B = map(int, input().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    def matrix_mul(a1, a2):
        res = [[0]* N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                s = sum(a1[r][i] * a2[i][c] for i in range(N))
                res[r][c] = s % 1000
        return res
    
    def power(n, arr):
        if n == 1:
            return arr
        if n % 2 == 0:
            half = power(n//2, arr)
            return matrix_mul(half, half)
        else:
            return matrix_mul(arr, power(n-1, arr))

    for row in power(B,A):
        print(*[r % 1000 for r in row])
        
    return 0

sol()