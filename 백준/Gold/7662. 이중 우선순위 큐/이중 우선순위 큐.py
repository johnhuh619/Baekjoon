import heapq
import sys

t = int(input())    # 입력 데이터 개수


for _ in range(t):
    
    k = int(input())    # 연산 개수
    
    min_pq = []
    max_pq = []
    
    visited = [False] * k
    nid = 0
    
    for i in range(k):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(min_pq, (num, nid))
            heapq.heappush(max_pq, (-num, nid))
            visited[nid] = True 
            nid += 1
        # D -1 => min 삭제
        # D 1 => max 삭제
        elif cmd == "D":
            if num == -1:
                # 삭제 표시 -> 진짜 삭제
                while min_pq and not visited[min_pq[0][1]]:
                    heapq.heappop(min_pq)
                if min_pq:
                    _, i = heapq.heappop(min_pq)
                    visited[i] = False # 삭제 표시
                
            else:
                # 삭제 표시 -> 진짜 삭제
                while max_pq and not visited[max_pq[0][1]]:
                    heapq.heappop(max_pq)
                if max_pq:
                    _, i = heapq.heappop(max_pq)
                    visited[i] = False # 삭제 표시
         
    # 데이터 정리.           
    while min_pq and not visited[min_pq[0][1]]:
        heapq.heappop(min_pq)
    while max_pq and not visited[max_pq[0][1]]:
        heapq.heappop(max_pq)

    if not min_pq:
        print("EMPTY")                
    else:
        print(-max_pq[0][0], min_pq[0][0])