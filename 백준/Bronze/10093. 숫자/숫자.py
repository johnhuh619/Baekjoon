def print_numbers_between(A, B):
    for i in range(A + 1, B):
        print(i, end=' ')

A, B = map(int, input().split())
if A > B:
    A, B = B, A

if A == B or B - A == 1:
    print(0)
else:
    print(B-A-1)
    print_numbers_between(A,B)

