n = input()
ans = set()
def sol(n):
  length = len(n)
  
  for i in range(0, length):
    for j in range(i, length):
      ans.add(n[i:j+1])

sol(n)
print(len(ans))