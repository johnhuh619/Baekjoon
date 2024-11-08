import sys
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))
res = [[0]*n for _ in range(n)]

def dfs(start,cur):
    for n_node in range(n):
        if matrix[cur][n_node] == 1 and res[start][n_node] == 0:
            res[start][n_node] = 1
            dfs(start,n_node)

for i in range(n):
    dfs(i,i)

for row in res:
    print(*row)
