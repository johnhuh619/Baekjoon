def is_odd(n):
  return n % 2 != 0

numbers= []
for _ in range(7):
  num = int(input())
  numbers.append(num)

odd_nums = list(filter(is_odd,numbers))
ans = sum(odd_nums)

if ans == 0:
  print(-1)
else:
  print(ans)
  print(min(odd_nums))