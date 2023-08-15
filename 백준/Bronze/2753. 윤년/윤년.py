A = int(input())
if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
    YEAR = 1  # 윤년
else:
    YEAR = 0  # 평년

print(YEAR)
