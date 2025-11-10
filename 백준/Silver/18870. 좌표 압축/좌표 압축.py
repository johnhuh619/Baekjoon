# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

def sol():
    N = int(input())
    ns = list(map(int, input().split()))
    sorted_set = sorted(set(ns))
    rank = {s: idx for idx, s in enumerate(sorted_set)}
    ans = [rank[n] for n in ns]
    print(' '.join(map(str, ans)))

sol()
    