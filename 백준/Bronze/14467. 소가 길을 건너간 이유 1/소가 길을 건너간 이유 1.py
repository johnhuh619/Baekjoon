n = int(input())
dic = {}
cnt = 0
for _ in range(n):
    cow, cow_p = map(int, input().split())
    if cow in dic and dic[cow] != cow_p:
        cnt += 1
        dic[cow] = abs(1-dic[cow])
    else:
        dic[cow] = cow_p
    
print(cnt)
