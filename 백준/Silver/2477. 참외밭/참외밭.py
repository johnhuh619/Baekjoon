from collections import defaultdict
n = int(input())
dirs = []
length = []
for _ in range(6):
    dir, l = map(int, input().split())
    dirs.append(dir)
    length.append(l)


max_r = 0
max_c = 0

for i in range(6):
    # 1: east 2: west
    if dirs[i] == 1 or dirs[i] == 2:
        if length[i] > max_r:
            max_r = length[i]
            r_idx = i
    else:
        if length[i] > max_c:
            max_c = length[i]
            c_idx = i

small = abs(length[(r_idx-1) % 6] - length[(r_idx+1) % 6]) * abs(length[(c_idx-1) % 6] - length[(c_idx+1) % 6])
ans = max_r*max_c - small
print(ans*n)

        
        
         