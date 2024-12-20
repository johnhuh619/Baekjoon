import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = {}
dic_int = {}
for i in range(1,N+1):
    t = input().strip()
    dic[t] = i
    dic_int[i] = t
for _ in range(M):
    t = input().strip()
    if t.isalpha():
        print(dic[t])
    else:
        print(dic_int[int(t)])
