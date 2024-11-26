import sys
input = sys.stdin.readline

def dfs(i):
    global ans
    if i==N:
        ans+=1
        return ans
    for j in range(N):
        if v1[j] == v2[i+j] == v3[i-j]==0:
            v1[j], v2[i+j], v3[i-j]= 1,1,1
            dfs(i+1)
            v1[j], v2[i+j], v3[i-j]= 0,0,0
            
N = int(input())
ans = 0
v1 = [0]*N
v2 = [0]*(2*N)
v3 = [0]*(2*N)
dfs(0)
print(ans)