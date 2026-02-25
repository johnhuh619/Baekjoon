n = int(input())
# 1 X => x에 point 버린다
# 2 => 가까운 pos 이동 -> point 획득 -> 반복

trash = []
pos = 0
tot = 0

def binary_search(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r) // 2
        if arr[mid] < target: 
            l = mid + 1
        else:
            r = mid
    return l

for _ in range(n):
    query = input().split()
    
    if query[0] == '1':
        x = int(query[1])
        trash.append(x)
        
    else:
        if not trash:
            continue
        
        trash.sort()
        idx = binary_search(trash, pos)       
        
        l = idx - 1
        r = idx
        
        while l >= 0 or r < len(trash):
            if l < 0:
                nxt = trash[r]
                r += 1
            
            elif r >= len(trash):
                nxt = trash[l]
                l -= 1
            
            else:
                dist_l = abs(pos - trash[l])
                dist_r = abs(pos - trash[r])

                if dist_l <= dist_r:
                    nxt = trash[l]
                    l -= 1
                else:
                    nxt = trash[r]
                    r += 1
            
            tot += abs(pos - nxt)
            pos = nxt
        trash.clear()

print(tot)