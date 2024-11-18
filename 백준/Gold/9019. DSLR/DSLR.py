import sys
from collections import deque
input = sys.stdin.readline

def bfs(a,b):
  visited = [False] * 10000
  q= deque()
  q.append((a,""))  # 현재 값, 명령어 문자열
  visited[a] = True
  while q:
    
    current, commands = q.popleft()
    if current == b:
      return commands

    next_d = (current*2) % 10000
    if not visited[next_d]:
      visited[next_d] = True
      q.append((next_d, commands+"D"))

    next_s = current -1 if current != 0 else 9999 
    if not visited[next_s]:
      visited[next_s] = True
      q.append((next_s, commands+"S"))

    next_l = current % 1000 * 10 + current // 1000
    if not visited[next_l]:
      visited[next_l] = True
      q.append((next_l, commands+"L"))      

    next_r = current % 10 * 1000 + current // 10
    if not visited[next_r]:
      visited[next_r] = True
      q.append((next_r, commands+"R"))

t = int(input())
for _ in range(t):
  a, b = map(int,input().split())
  print(bfs(a,b))
