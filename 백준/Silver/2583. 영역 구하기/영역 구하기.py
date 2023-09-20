from collections import deque


def bfs(i,j):
    q = deque()
    q.append((i,j))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= ny < m and 0 <= nx < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny,nx))
                cnt += 1
    return cnt

m, n, k = map(int,input().split())
visited = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = 1
res = []
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            res.append(bfs(i,j))
print(len(res))
# 오름차순으로 정렬 후 새로운 리스트로 리턴. 이 때 언패킹 해서 개별적 인자로 전달함.
print(*sorted(res))