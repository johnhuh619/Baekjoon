n, m = map(int, input().split())
cows = list(map(int, input().split()))

def calc(i):
    return cows[i%n] * cows[(i+1)%n] * cows[(i+2)%n] * cows[(i+3)%n]

tot = 0
fixed = list(map(int,input().split()))

# 초기값
for i in range(n):
    tot += calc(i)
    

# 10^5
for f in fixed:
    f -= 1
    
    for d in range(4):
        tot -= calc(f-d)
    
    cows[f] *= -1
    
    # 2*10^5
    for d in range(4):
        tot += calc(f-d)
        
    print(tot)
        