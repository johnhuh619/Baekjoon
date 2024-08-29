N = list(map(int, input().split()))
answer = 0
for i in N:
    answer += i*i
 
print(answer % 10)