from collections import deque

N, K = map(int, input().split())
visited = [0] * (10**5 + 1)



def solution():

    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j < 10**5 + 1 and not visited[j]:
                visited[j] = visited[x] + 1
                queue.append(j)

solution()
