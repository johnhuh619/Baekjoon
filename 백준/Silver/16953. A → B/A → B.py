from collections import deque
a, b = map(int, input().split())
# 탑->바텀 bfs로 구현하면 될듯
def bfs(a,b):
    q = deque()
    q.append((b,0))
    while q:
        current, cnt = q.popleft()
        if current == a:
            return cnt+1
        if current > a:
            if current % 2 == 0:
                q.append((current//2, cnt+1))
            if current % 10 == 1:
                q.append((current//10, cnt+1))
                
    return -1

print(bfs(a,b))