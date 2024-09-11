
N, M = map(int, input().split())
arr = list(map(int,input().split()))

def sol(N, M, arr):
    start, end = 0, 0
    sum_ = arr[0]
    cnt = 0
    while True:
        if sum_ < M:
            end += 1
            if end >= N:
                break
            sum_ += arr[end]
        elif sum_ == M:
            cnt += 1
            sum_ -= arr[start]
            start += 1
        else:
            sum_ -= arr[start]
            start += 1
    return cnt
print(sol(N, M, arr))

