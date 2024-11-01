text = input().split("-")
num = []
for i in text:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum)
n = num[0]
for i in num:
    n -= i
n+=num[0]
print(n)