# 맨해튼 거리 |r1 -r2| + |c1 - c2|
# 1. p 근거리 p 확인, 도달 불가능 하다면 조건 거리 준수한 셈.
# 2. 조건 거리 체크
# 3. ok -> 이 p 주변 p 확인. 1->2 반복
from collections import deque

def solution(places):
    def bfs(room, x, y):
        q = deque()
        q.append((x, y, 0))
        visited = [[False] * 5 for _ in range(5)]
        visited[x][y] = True
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        while q:
            cx, cy, dist = q.popleft()
            if dist > 0 and room[cx][cy] == 'P':
                return False

            if dist == 2:
                continue
            
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if room[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append((nx,ny,dist+1))
        return True     
        
    answer = []
    for room in places:
        check = 1
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if not bfs(room,i,j):
                        check = 0
                        break
            if check == 0:
                break
        answer.append(check)
                    

    return answer