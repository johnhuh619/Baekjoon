from collections import deque
n, k = map(int ,input().split())

def y_prob(n, k):
    q = deque([i for i in range(1,n+1)])
    ans = []
    while q:
        for _ in range(k-1):
            q.append(q.popleft())
        ans.append(q.popleft())        
    return ans

print("<" +', '.join(map(str, y_prob(n,k)))+">" )