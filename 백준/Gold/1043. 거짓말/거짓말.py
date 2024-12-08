import sys
input = sys.stdin.readline
N, M = map(int, input().split())
t = set(map(int,input().split()[1:]))
party = [set(map(int,input().split()[1:])) for _ in range(M)]

can = [False] *M
# t 가 있는 배열의 동일 멤버를 t에 갱신해줌.
for _ in range(M):
  for i, people in enumerate(party):
    if people & t:
      t.update(people)
res = 0
for i in party:
  if not(i & t):
    res += 1

print(res)