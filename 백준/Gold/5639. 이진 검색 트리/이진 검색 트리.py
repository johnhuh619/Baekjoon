import sys

sys.setrecursionlimit(10 ** 6)

tree = list(map(int, sys.stdin.read().split()))

def sol(start, end):
    if start >= end:
        return 
    
    root = tree[start]
    nxt_root_idx = start+1
    while nxt_root_idx < end and tree[nxt_root_idx] < root:
        nxt_root_idx+=1
    sol(start+1, nxt_root_idx)
    sol(nxt_root_idx, end)
    print(root)

sol(0,len(tree))