import sys
n = int(input())
oasis = [int(sys.stdin.readline()) for _ in range(n)]
stack = [] # (키, 키가 같은 경우를 count)로 append
ans = 0

for i in oasis:
    while stack and stack[-1][0] < i:
        ans += stack.pop()[1]
    if not stack:
        stack.append((i,1))
        continue
    if stack[-1][0] == i:
        same = stack.pop()[1]
        ans += same
        if stack: 
            ans += 1
        stack.append((i,same+1))
    else:
        stack.append((i,1))
        ans += 1 # 클 경우 그놈과도 묶여야 함.


print(ans)