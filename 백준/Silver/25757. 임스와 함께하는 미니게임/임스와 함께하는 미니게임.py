import sys


# 중복 거르기
def test():
    n, k = sys.stdin.readline().split()
    # set 이용 중복 제거
    people = set()
    for _ in range(int(n)):
        people.add(sys.stdin.readline().rstrip())
    p = len(people)
    # 2인겜
    if k == 'Y':
        print(p)
    # 3인겜
    elif k == 'F':
        print(p//2)
    # 4인겜
    else:
        print(p//3)


test()
