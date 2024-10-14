from collections import deque

N, K = map(int, input().split())

visited = [-1]*100001
path = []
def bfs(start, target):
    queue = deque()
    queue.append((N,0)) # (위치, time)

    while queue:
        current, time = queue.popleft()
        if current == target:
            idx = current
            while idx != start:
                path.append(idx)
                idx = visited[idx]
            path.append(start)
            return time
        # +1, -1, *2
        if current+1 < 100001 and visited[current+1] == -1: # 범위 안 & visit 안했을 때
            queue.append((current+1, time+1))
            visited[current+1] = current    # 현재 위치의 값 = 이동 전 위치
        if current-1 >= 0 and visited[current-1] == -1:
            queue.append((current-1, time+1))
            visited[current-1] = current
        if current*2 < 100001 and visited[current*2] == -1:
            queue.append((current*2, time+1))
            visited[current*2] = current

print(bfs(N,K))
print(*path[::-1])  # unpacking + 뒤에서부터 출력
