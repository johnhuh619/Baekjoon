from collections import deque
num = int(input())
cnt = 0

for _ in range(num):
    a = input()
    stack = deque()
    flag = 0
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        flag = 1
        print("YES")
    else:
        print("NO")
