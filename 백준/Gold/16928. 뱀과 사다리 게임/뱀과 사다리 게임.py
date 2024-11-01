from collections import deque
n,m = map(int, input().split())
length = n+m
board = list(range(101)) 
ladders = []
for i in range(length):
    x, y = map(int,input().split())
    ladders.append((x,y))
for x, y in ladders:
    board[x] = y

queue = deque([(1,0)])
visited = [False]*101
visited[1] = True
roll = 0
while queue:
    pos, roll = queue.popleft()
    if pos == 100:
        break
    for dice in range(1,7):
        next_pos = pos + dice
        if next_pos <= 100:
            next_pos = board[next_pos]
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, roll + 1))

print(roll)