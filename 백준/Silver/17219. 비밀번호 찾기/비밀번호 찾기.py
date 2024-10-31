n, m = map(int, input().split())
add = {}
for _ in range(n):
    site, pwd = input().split()
    add[site] = pwd

for _ in range(m):
    print(add[input()])
