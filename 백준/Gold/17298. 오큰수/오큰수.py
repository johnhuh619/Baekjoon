import sys
n = int(input())
numbers = list(map(int,sys.stdin.readline().split()))
ans = [-1]*n
stack = []

for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i]:
        ans[stack.pop()] = numbers[i]
    stack.append(i)
print(*ans)
