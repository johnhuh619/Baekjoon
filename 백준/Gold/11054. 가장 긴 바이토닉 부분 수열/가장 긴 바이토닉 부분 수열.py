
def sol():
    N = int(input())
    nums = list(map(int, input().split()))
    
    dp = [0]*N
    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j]+1, dp[i])
    
    dp_back = [0]*N
    arr_back = nums[::-1]
    
    for i in range(1,N):
        for j in range(i):
            if arr_back[i] > arr_back[j]:
                dp_back[i] = max(dp_back[j]+1, dp_back[i])

    ans = 0
    for i in range(N):
        ans = max(ans, dp[i]+dp_back[::-1][i])
    return ans+1
print(sol())
                

            
    
        