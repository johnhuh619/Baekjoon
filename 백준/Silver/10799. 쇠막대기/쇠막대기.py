import sys

n = list(map(str,sys.stdin.readline().strip()))
stack =[]
cnt = 0

for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])
    # 레이저
    elif n[i-1] == '(': 
        stack.pop()
        cnt+= len(stack)
    # 파이프 끝
    else: 
        stack.pop()
        cnt+=1
print(cnt)