# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
# 그 다음 줄부터 각각의 테스트 케이스에 대해 
# 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 
# 두 배추의 위치가 같은 경우는 없다.

from collections import deque

def sol():
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    visited = [[False]*M for _ in range(N)]
    cnt = 0

    def bfs(i,j):
        dx= [1,-1,0,0]
        dy = [0,0,1,-1]
        q = deque([(i,j)])

        while q:
            y, x = q.popleft()
            for n in range(4):
                nx = x + dx[n]
                ny = y + dy[n]
                if 0 > nx or nx >= M or 0 > ny or ny >= N:
                    continue
                if not visited[ny][nx] and field[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))
        
        
    for y in range(N):
        for x in range(M):
            if field[y][x]  == 1 and not visited[y][x]:
                bfs(y,x)
                cnt +=1
    return cnt        

def main():
    T = int(input())
    for _ in range(T):
        print(sol())

main()