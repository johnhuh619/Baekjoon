n = int(input())
switch = list(map(int,input().split()))
m = int(input())

def toggle(i):
    switch[i] = 1 - switch[i]
    
def man(num):
    i = num -1
    while i < n:
        toggle(i)
        i += num
        

def woman(num):
    i = num -1
    toggle(i)
    l, r = i-1, i+1
    while l >= 0 and r < n and switch[l] == switch[r]:
        toggle(l)
        toggle(r)
        l -= 1
        r += 1


for _ in range(m):    
    gen, num = map(int, input().split())
    if gen == 1:
        man(num)
    else:
        woman(num)

    
for i in range(n):
    print(switch[i], end = ' ')
    if (i+1) % 20 == 0:
        print()