A, B, C = map(int, input().split())

num = [A, B, C]
MIN = MAX = MID = 0

MIN = min(num)
MAX = max(num)
MID = sum(num) - MIN - MAX
print(MIN, MID, MAX)
