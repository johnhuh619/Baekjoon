from collections import deque
import sys
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
q = deque()

def push (a,q):
    q.append(a)

def pop(q):
    if not q:
        print(-1)
    else:
        print(q.popleft())

def size(q):
    print(len(q))

def empty(q):
    if not q:
        print(1)
    else:
        print(0)

def front(q):
    if not q:
        print(-1)
    else:        
        print(q[0])
def back(q):
    if not q:
        print(-1)
    else:
        print(q[-1])

num = int(input())
for _ in range(num):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        try:
            push(command[1],q)
        except ValueError:
            print("Invalid number format")
    elif command[0] == "pop":
        pop(q)
    elif command[0] == "size":
        size(q)
    elif command[0] == "empty":
        empty(q)
    elif command[0] == "front":
        front(q)
    elif command[0] == "back":
        back(q)