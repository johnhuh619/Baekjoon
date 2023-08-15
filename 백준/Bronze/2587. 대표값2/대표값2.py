numbers= []
for _ in range(5):
  num = int(input())
  numbers.append(num)
MEAN = int(sum(numbers) / 5)
numbers.sort()
MID = numbers[2]
print(MEAN)
print(MID)