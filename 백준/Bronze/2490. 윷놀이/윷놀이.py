def dice_compare(dice):
  ans = sum(dice)
  if ans == 4:
    return "E"
  elif ans == 3:
    return "A"
  elif ans == 2:
    return "B"
  elif ans == 1:
    return "C"
  else:
    return "D"

results = []
for _ in range(3):
  dice = list(map(int, input().split()))
  results.append(dice_compare(dice))

for i in results:
  print(i)
