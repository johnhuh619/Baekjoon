n,r,c= map(int, input().split())
def z(n,r,c,res):
    length = 2**n
    half = length//2
    if n == 1:
        print(2*r+c+res)
        return
    if r>=half and c>= half: # 4
        z(n-1, r - half, c-half, res + 3*half*half) # 1+2+3사분면 + 새로시작
    elif r >= half > c: # 3
        z(n-1, r-half, c, res + 2*half*half)  # 1+2사분면 + 새로시작
    elif r < half <= c: # 2
        z(n-1, r, c - half, res + half*half) # 1사분면 + 새로 시작
    else:   # 1
        z(n-1, r, c, res)
        
z(n,r,c,0)