from itertools import combinations
def roll(dices):
    sums = [0]
    for dice in dices:
        sums = [d1 + d2 for d1 in sums for d2 in dice]
    return sums
def bi(arr, x):
    """ arr 은 정렬된 list, x보다 작거나 같은 개수 반환 """
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r) // 2
        if arr[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l
        
def solution(dice):
    answer = []
    
    n = len(dice)
    idx = list(range(n))
    half = n // 2
    best = -1
    best_pick = None
    for a_idx in combinations(idx, half):
        b_idx = [ i for i in idx if i not in a_idx]
        
        a_sums = roll([dice[i] for i in a_idx])
        b_sums = roll([dice[i] for i in b_idx])
        
        b_sums.sort()
        
        win = 0
        for s in a_sums:
            win += bi(b_sums, s-1)
            
        if win > best:
            best = win
            best_pick = a_idx        
    return [ i+1 for i in best_pick]