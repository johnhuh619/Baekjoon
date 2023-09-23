from collections import deque
import sys

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(c,a,b):
  q = deque()
  q.append((c,a,b))
  visited[c][a][b] = 1
  while q:
    c, a, b = q.popleft()
    for i in range(6):
      nx = dx[i] + a
      ny = dy[i] + b
      nz = dz[i] + c
      if 0<=nz<z and 0<=nx<x and 0<=ny<y:
        if graph[nz][nx][ny] == 'E':
          print('Escaped in',visited[c][a][b],'minute(s).')
          return
        if visited[nz][nx][ny] == 0 and graph[nz][nx][ny] == '.':
          visited[nz][nx][ny] = visited[c][a][b] + 1
          q.append((nz,nx,ny))
  print("Trapped!")
    
while True:
  z, x, y = map(int, input().split())

  if z == 0 and y == 0 and x == 0:
    break

  graph = [[[]*y for _ in range(x)] for _ in range(z)]
  visited = [[[0]*y for _ in range(x)] for _ in range(z)]

  for i in range(z):
    graph[i] = [list(input()) for i in range(x)]
    input()

  for i in range(z):
    for j in range(x):
      for k in range(y):
        if graph[i][j][k] == 'S':
          bfs(i,j,k)

