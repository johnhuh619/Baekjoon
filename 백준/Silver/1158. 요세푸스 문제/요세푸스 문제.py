from collections import deque
n, k = map(int,input().split())

q = deque([i for i in range(1,n+1)])
ans = []
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(str(q.popleft()))        
    
print(f"<{', '.join(ans)}>")