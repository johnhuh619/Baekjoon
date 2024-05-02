import sys
from collections import defaultdict

# 크로스 컨트리
# 4 <= x <= 12 km
# len -> 6
# [0]+[1]+[2]+[3] = 점수
# len < 6 이면 count X
# a 점수 = b 점수 -> a[4] <-> b[4]

# T = test case
# 반복 ->
# 1. N = 총 횟수
# 2. number line => 팀 번호로 제시됨

T = int(input())

for i in range(T):
    N = int(input())
    team = list(map(int, sys.stdin.readline().rstrip().split()))
    manage = defaultdict(lambda: [0, [], 0])
    for j in range(N):
        manage[team[j]][0] += 1
    contain = set(k for k, v in manage.items() if v[0] < 6)
    grade = 1
    for j in range(N):
        if team[j] not in contain:
            manage[team[j]][1].append(grade)
            if len(manage[team[j]][1]) <= 4:
                manage[team[j]][2] += grade
            grade += 1
    ans = []
    for k, v in manage.items():
        if len(v[1]) != 0:
            ans.append([k, v[1][4], v[2]])
    a = sorted(ans, key=lambda x: (x[2], x[1]))
    print(a[0][0])