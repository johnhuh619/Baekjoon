from collections import deque
t = int(input())

def find(l, k, d):
    m = max(l)
    cnt = 0
    while l:
        top = l.popleft() 
        cur_max = max(d[i] for i in l) if l else -1
        if d[top] >= cur_max:
            cnt += 1
            if top == k:
                return cnt
        else:
            l.append(top)
    

for _ in range(t):

    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    l = deque(range(n))
    
    d = {i: q[i] for i in range(n)}        
        
    print(find(l,m,d))

