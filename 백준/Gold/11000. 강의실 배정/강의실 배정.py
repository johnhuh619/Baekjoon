import sys
import heapq
input = sys.stdin.readline
N = int(input())
time = []

for _ in range(N):
    time.append(list(map(int,input().split(' '))))
    
time.sort(key=lambda x: (x[0], x[1]))

# 가장 빠른 종료 시간을 힙에서 출력한다
# 힙을 사용하는 이유는 자동 정렬이 되기 때문이다.
heap = [time[0][1]]
for i in range(1,N):
    # 만약 가장 빠른 종료 시간 <= 현재 강의 시작 시간
    if heap[0] <= time[i][0]:
        # 강의실을 이어서 사용이 가능하다 => 종료 시간을 힙에서 제거
        heapq.heappop(heap)
    # 현재 강의의 종료 시간을 힙에 추가
    # 현재 진행 중인 강의의 종료 시간을 체크해 줘야 하니까.
    heapq.heappush(heap, time[i][1])

print(len(heap))