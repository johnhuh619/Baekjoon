k, n = map(int, input().split())
wires = [int(input()) for x in range(k)]

def cut_wire(cut):
    tot = 0
    for wire_len in wires:
        tot += wire_len // cut
    return n <= tot

l = 1
r = max(wires) + 1
while l < r:
    mid = (l+r) //2
    if cut_wire(mid):
        l = mid +1
    else:
        r = mid
        
print(l-1)