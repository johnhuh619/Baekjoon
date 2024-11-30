n,m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]

house = []
chicken = []
selected = []
min_distance = float('inf')

def dfs(idx, cnt):
  global min_distance

  if cnt == m:
    tot_distance = 0
    for r,c in house:
      distance = float('inf')
      for cr, cc in selected:
        distance = min(distance, abs(r-cr)+abs(c-cc))
      tot_distance += distance
    min_distance = min(min_distance,tot_distance)
    return

  for i in range(idx, len(chicken)):
    selected.append(chicken[i])
    dfs(i+1,cnt+1)
    selected.pop()

for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      house.append((i,j))
    elif city[i][j] == 2:
      chicken.append((i,j))

dfs(0,0)
print(min_distance)