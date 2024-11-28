
n = int(input())
numbers = list(map(int,input().split()))
visited = [False for _ in range(n)]
cnt = 0
res = []
def dfs():
    global cnt
    
    if len(res) == n:
        tmp = 0
        for i in range(n-1):
            tmp += abs(res[i]-res[i+1])
        cnt = max(cnt,tmp)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            res.append(numbers[i])
            dfs()
            res.pop()
            visited[i] = False

dfs()
print(cnt)