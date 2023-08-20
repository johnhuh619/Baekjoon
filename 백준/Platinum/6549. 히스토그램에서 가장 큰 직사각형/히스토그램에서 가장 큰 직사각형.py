import sys
from collections import deque
while True:
  graph = list(map(int,sys.stdin.readline().split()))
  n = graph.pop(0)
  if n == 0:
    break
  stack = deque()
  max_result = 0
  # 길이 * (index - stack(index임) -1)
  for i in range(n):
    while stack and graph[stack[-1]] > graph[i]:
      temp = stack.pop()

      if not stack:
        width = i
      else:
        width = i - stack[-1] - 1
      new = graph[temp]*width
      
      if max_result < new:
        max_result = new
    stack.append(i)
  while stack:
    temp = stack.pop()
    if not stack:
      width = n
    else:
      width = n - stack[-1] - 1
    new = graph[temp]*width
    if max_result < new:
      max_result = new
  print(max_result)