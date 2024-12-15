n,m = map(int,input().split())
dic = {}
for _ in range(n):
  dic[input()] = 1
cnt = 0
for _ in range(m):
  word = input()
  if word in dic:
    cnt+=1
print(cnt)