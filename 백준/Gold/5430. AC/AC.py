import sys
from collections import deque

num = int(input())
for _ in range(num):
    cmd = sys.stdin.readline().rstrip()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:
        arr = deque()

    err = False
    cnt = 0
    for i in cmd:
        if i == "R":
            cnt+=1
        else:
            if not arr:
                err = True
                print("error")
                break
            elif cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    if not err:
        if cnt % 2 == 0:
            print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("["+",".join(arr)+"]")