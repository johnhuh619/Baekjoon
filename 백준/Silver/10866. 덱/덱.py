from collections import deque
import sys

q = deque()

def push_front(a, q):
    q.appendleft(a)

def push_back(a, q):
    q.append(a)

def pop_front(q):
    if not q:
        print(-1)
        return
    print(q.popleft())

def pop_back(q):
    if not q:
        print(-1)
        return
    print(q.pop())

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
        return
    print(q[0])

def back(q):
    if not q:
        print(-1)
        return
    print(q[-1])

num = int(input())
for _ in range(num):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        push_front(int(command[1]), q)
    elif command[0] == "push_back":
        push_back(int(command[1]), q)
    elif command[0] == "pop_front":
        pop_front(q)
    elif command[0] == "pop_back":
        pop_back(q)
    elif command[0] == "size":
        size(q)
    elif command[0] == "empty":
        empty(q)
    elif command[0] == "front":
        front(q)
    elif command[0] == "back":
        back(q)
