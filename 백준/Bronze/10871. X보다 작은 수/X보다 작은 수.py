n,m = map(int,input().split())
numbers = list(map(int,input().split()))
res = ''
for num in numbers:
    if num < m:
        res+=str(num)
        res+=' '
    
print(res[:-1])