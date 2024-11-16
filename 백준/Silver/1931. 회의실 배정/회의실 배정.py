import sys
n = int(sys.stdin.readline())
time = []
for _ in range(n):
    s, e = map(int,sys.stdin.readline().split())
    time.append((s,e))
time.sort(key = lambda x: x[0])
time.sort(key = lambda x: x[1])

cnt = 1
end_time = time[0][1]  # 첫 회의의 끝나는 시간
for i in range(1, n):
    if time[i][0] >= end_time:  # 현재 회의 시작 시간이 이전 회의 종료 시간보다 같거나 늦으면 선택
        cnt += 1
        end_time = time[i][1]

print(cnt)