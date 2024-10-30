import sys
m, n = map(int, sys.stdin.readline().split())
# m 이상 n 이하의 소수를 모두 출력하는 프로그램을 작성하시오.
prime_num = []
for i in range(m, n+1):
    if i == 1:
        continue
    condition = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            condition = False
            break
    # 메모리 고려해서 바로 출력해보기
    if condition:
        print(i)