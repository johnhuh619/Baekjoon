n,m = map(int,input().split())
numbers = list(map(int,input().split()))
res = ' '.join(str(num) for num in numbers if num < m)
print(res)
    