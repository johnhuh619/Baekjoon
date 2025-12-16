from collections import deque
def to_deque(s):
    if s == "[]":
        return deque()
    return deque(int(x) for x in s.strip('[]').split(',') if x)

def from_list(arr):
    return ("[" + ','.join(map(str,arr)) + "]")

def cmd_exec(cmd, q):
    rev = False
    for c in cmd:
        if c == "R":
            rev = not rev
        elif c == "D":
            if not q:
                return "error"    
            if rev:
                q.pop()
            else:
                q.popleft()
    if rev:
        q.reverse()                
    return from_list(q)

def test():
    cmd = input()
    length = int(input())
    s = input().strip()
    q = to_deque(s)
    print(cmd_exec(cmd, q))
    

n = int(input())
for _ in range(n):
    test()


