import sys
input = sys.stdin.readline

def preprocess_sieve(end):
    # 에라토스테네스의 체로 소수 판별 배열 생성
    num = [True] * (end + 1)
    num[0] = False  # 0과 1은 소수가 아님

    for i in range(2, int(end**0.5) + 1):
        if num[i]:
            for j in range(i * i, end + 1, i):
                num[j] = False

    # 소수 개수의 누적합 배열 생성
    prime_prefix = [0] * (end + 1)
    for i in range(1, end + 1):
        prime_prefix[i] = prime_prefix[i - 1] + (1 if num[i] else 0)

    return prime_prefix

# 입력
n, m = map(int, input().split())

# 최대 값까지의 소수 누적합 배열 생성
prime_prefix = preprocess_sieve(n)

for _ in range(m):
    i, j = map(int, input().split())
    print(prime_prefix[j] - prime_prefix[i - 1])