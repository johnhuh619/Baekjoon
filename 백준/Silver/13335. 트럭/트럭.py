from collections import deque
n, w, l = map(int, input().split())
log = deque(map(int,input().split()))

# w == birdge_len
bridge = deque([0]*w)
time = 0
tot = 0
while bridge:
    time += 1
    tot -= bridge.popleft()
    
    if log:
        if tot + log[0] <= l:
            t = log.popleft()
            tot += t                
            bridge.append(t)
        else:
            bridge.append(0)

print(time)

