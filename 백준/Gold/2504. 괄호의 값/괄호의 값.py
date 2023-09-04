import sys
from collections import deque

line = list(input())
stack = []
ans = 0
cnt = 1
for i in range(len(line)):
    l = line[i]
    if l == '(':
        stack.append(l)
        cnt *= 2
    elif l == '[':
        stack.append(l)
        cnt *= 3
    elif l == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if line[i-1] == '(':
            ans += cnt
        cnt //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if line[i-1] == '[':
            ans+=cnt    
        cnt //= 3
        stack.pop()
if stack:
    print(0)
else:
    print(ans)