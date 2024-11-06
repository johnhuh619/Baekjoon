import sys
n, m = map(int,input().split())
tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
        
    left = 0
    for i in tree:
        if i >= mid:
            left += i - mid
    if left >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)