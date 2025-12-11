from collections import deque
n, k = map(int,input().split())

# cur = x
# 1) x+1
# 2) x-1
# 3) x*2
MAX = 2000000
visited = [False]*MAX

def bfs():
    q = deque([(n,0)])
    
    while q:
        cx, cnt = q.popleft()
        if cx == k:
            return cnt
        
        for nx in [cx + 1, cx -1, cx*2]:
            if MAX > nx >= 0 and visited[nx] == False:
                visited[nx] = True
                q.append((nx, cnt+1))


print(bfs())