# 2 <-> 6 / 6 <-> 2
from collections import deque
gears = [deque(map(int, input().rstrip())) for _ in range(4)]

def spin(idx, dir):
    # 1 시계 / -1 반시계
    spinner = [0] * 4
    idx -= 1
    spinner[idx] = dir
    
    for i in range(idx, 3):
        if gears[i][2] != gears[i+1][6]:
            spinner[i+1] = -spinner[i]
        else:
            break
    
    for i in range(idx,0,-1):
        if gears[i][6] != gears[i-1][2]:
            spinner[i-1] = -spinner[i]
        else:
            break
    
    for i, d in enumerate(spinner):
        if d == 1:
            g = gears[i].pop()
            gears[i].appendleft(g)
        if d == -1:
            g = gears[i].popleft()
            gears[i].append(g)
    
            
k = int(input())
for _ in range(k):
    idx, dir = map(int, input().split())
    spin(idx,dir)
    
ans = 0
for i in range(4):
    if i == 0:
        ans += gears[i][0]
    else:
        ans += gears[i][0] * 2 ** i
    
print(ans)
    

