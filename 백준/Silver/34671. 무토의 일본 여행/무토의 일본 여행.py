import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
graph = {}
for _ in range(m):
    a, b, w = map(int, input().split())
    if a > b:
        a, b = b, a
    key = (a, b)
    res = graph.get(key, 0)
    if res == 0 or w < res:
        graph[key] = w
        

for _ in range(q):
    s, e = map(int,input().split())
    if s > e:
        s, e = e, s
    ans = graph.get((s,e), -1)
    print(ans)
