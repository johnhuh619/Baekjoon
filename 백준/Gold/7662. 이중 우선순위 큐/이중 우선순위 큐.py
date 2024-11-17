import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    min_q = []
    max_q = []
    k = int(sys.stdin.readline())
    alive = [False]*k
    for i in range(k):
        s, n = sys.stdin.readline().split()
        if s == "I":
            #이중 heapq 여기 들어감
            heapq.heappush(min_q, (int(n), i))  
            heapq.heappush(max_q,(int(n)*-1,i))
            alive[i] = True
        else:
            if int(n) == -1:
                if min_q:
                    alive[heapq.heappop(min_q)[1]] = False
            else:
                if max_q:
                    alive[heapq.heappop(max_q)[1]] = False
        while min_q and alive[min_q[0][1]] == False:
            heapq.heappop(min_q)
        while max_q and alive[max_q[0][1]] == False:
            heapq.heappop(max_q)
            
    if len(min_q) == 0:
        print("EMPTY")
    else:
        print(-max_q[0][0], min_q[0][0])
    
                    

