n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

low, high = 0, n-1
cnt = 0
while low < high:
    if data[low] + data[high] >= m:
        cnt += 1
        low += 1
        high -= 1
    else:
        low += 1

print(cnt)        