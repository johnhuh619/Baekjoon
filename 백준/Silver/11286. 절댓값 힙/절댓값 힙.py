import sys, heapq
# 튜플을 이용하면, 앞에거 먼저 비교함. if 앞에가 같다? -> 뒤에거 비교
# 따라서 절댓값 값을 먼저 넣고, 그다음 넘을 넣음.
abs_heap = []
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(abs_heap, (abs(num),num))
    else:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)