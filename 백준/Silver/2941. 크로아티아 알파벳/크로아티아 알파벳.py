arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
a = input()
answer = 0

for e in arr:
    while a.find(e)> -1:
        a = a.replace(e, ' ')
answer += len(a)    

print(answer)