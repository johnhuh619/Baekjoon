from itertools import combinations

dwrfs = [int(input()) for _ in range(9)]
def find_dwrf(dwrf):
    for i in combinations(dwrf, 7):
        if sum(i) == 100:
          return i
 
result = find_dwrf(dwrfs)
for i in sorted(result):
   print(i)