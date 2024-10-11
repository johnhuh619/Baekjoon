from collections import deque
def bfs():
    queue = deque()
    queue.append((home_x,home_y))
    while queue:
        x, y = queue.popleft()
        if abs(x-festa_x) + abs(y-festa_y) <= 1000: # 맥주를 리필할 필요가 있는가? No!
            print('happy')
            return 0
        else:
            for i in range(N):  # 편의점 개수만큼 반복
                if not visited[i]: # i번째 편의점을 방문 안했다면?
                    nx, ny = conv[i] # 해당 위치 편의점 좌표 뽑기
                    if abs(x-nx)+abs(y-ny) <= 1000:
                        queue.append((nx,ny)) # nx,ny 좌표 위치로 이동
                        visited[i] = 1  # 방문 체크
    print('sad')
    return 0
            

    return 0
T= int(input())
for _ in range(T):
    N = int(input())
    conv = []
    home_x, home_y = map(int,input().split()) # 상근이네 집 좌표
    for i in range(N):  # 편의점들 좌표
        a,b = map(int,input().split())
        conv.append((a,b))
    festa_x, festa_y = map(int,input().split()) # 락페 좌표
    visited = [0 for _ in range(N+1)]
    bfs()




