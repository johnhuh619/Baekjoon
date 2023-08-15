def dice_compare(dice):
  dice.sort()

  if dice[0] == dice[2]:
    prize = 10000 + dice[0] * 1000
  elif dice[0] == dice[1] or dice[1] == dice[2]:
    prize = 1000 + dice[1] * 100
  else:
    prize = dice[2] * 100
  return prize

dice = list(map(int, input().split()))
print(dice_compare(dice))



