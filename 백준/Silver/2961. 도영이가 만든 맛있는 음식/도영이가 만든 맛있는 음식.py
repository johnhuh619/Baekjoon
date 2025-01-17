N = int(input())
# arr[0] = 신맛 , arr[1] = 쓴맛
arr =[list(map(int,input().split())) for _ in range(N)]
# 신맛의곱 = 신맛 , 쓴맛의 합 = 쓴맛

ans = 1e9
# S-B
def bt(idx, s, b, cnt):
    global ans
    if cnt > 0:        
        ans = min(ans, abs(s-b))
    
    if idx == N:
        return
    
    bt(idx+1, s*arr[idx][0], b+arr[idx][1], cnt+1)
    
    bt(idx+1, s, b, cnt)
bt(0,1,0,0)
print(ans)
  
        

    
