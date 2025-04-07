import sys

sys.setrecursionlimit(10 ** 6)

tree = list(map(int, sys.stdin.read().split()))


def sol(start, end):
    if start >= end:
        return
    root = tree[start]
    split = start+1
    # 좌측 / 우측 서브 트리 분리
    while split < end and tree[split] < root:
        split += 1
    sol(start+1, split)
    sol(split, end)
    print(root)

sol(0,len(tree))

    