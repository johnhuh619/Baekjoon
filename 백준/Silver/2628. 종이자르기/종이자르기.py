import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cut = int(input())

row_cut = [0, m]
col_cut = [0, n]

for _ in range(cut):
    
    t, cut_n = map(int, input().split())
    if t == 0:
        row_cut.append(cut_n)
    else:
        col_cut.append(cut_n)


row_cut.sort()
col_cut.sort()

r_max = 0
for i in range(1, len(row_cut)):
    r_max = max(r_max, row_cut[i] - row_cut[i-1])

l_max = 0
for j in range(1, len(col_cut)):
    l_max = max(l_max, col_cut[j] - col_cut[j-1])

print(r_max*l_max)