import sys
from collections import deque
# 1. input 받기

N, Q = map(int, input().split())
ice_graph = []
for _ in range(2**N):
    ice_graph.append(list(map(int,input().split())))
L = list(map(int, input().split()))


# 2. 배열의 회전
def spin_arr(graph, L):
    s = 2**L
    size = len(graph)
    new_graph = [[0] * size for  _ in range(size)]
    for i in range(0, size, s):     # row
        for j in range(0, size, s): # column
            block = [row[j:j+s] for row in graph [i:i+s]]       # 박스 추출
            rotate_block = [list(x) for x in zip(*block[::-1])] # reverse -> 전치 = 시계방향 90도 회전
            for x in range(s):
                new_graph[i+x][j:j+s] = rotate_block[x]
    return new_graph

# 3. 회전 + 얼음 녹음-
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def melt_ice(graph):
    size = len(graph)
    decrease = []
    for i in range(size):
        for j in range(size):
            if graph[i][j] > 0:
                ice_count = 0
                for n in range(4):
                    nx = i + dx[n]
                    ny = j + dy[n]
                    if 0 <= nx < size and 0 <= ny < size:
                        if graph[nx][ny] > 0:
                            ice_count += 1
                if ice_count < 3:
                    decrease.append((i,j))
    for i,j in decrease:
        graph[i][j] -= 1
    return graph

# 4. 모든 단계에서 [회전 -> 얼음 녹이기] 를 진행시켜준다.
for l in L:
    ice_graph = spin_arr(ice_graph,l)
    ice_graph = melt_ice(ice_graph)

# 5. 이제 가장 큰 얼음 덩어리를 구한다.
# 탐색해서 개수 더해서, 가장 큰 숫자로 반복 갱신 해준다
# 일단 먼저 bfs 구현
def bfs(graph, visited, i, j):  # 그래프, 방문여부, 시작 좌표(i,j)
    size = len(graph)
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < size and 0 <= ny < size:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    cnt += 1
                
    return cnt
# 6-1. 가장 큰 얼음 덩이를 구하기 위한 반복 갱신 해주기
# 6-2. sum_ice 구해주기
sum_ice = 0
max_size = 0
size = len(ice_graph)
visited = [[False]*size for _ in range(size)]
for i in range(size):
    for j in range(size):
        sum_ice += ice_graph[i][j]
        if ice_graph[i][j] > 0 and visited[i][j] == False:
            ice_size = bfs(ice_graph,visited,i,j)
            if ice_size > max_size:
                max_size = ice_size

print(sum_ice)
print(max_size)
