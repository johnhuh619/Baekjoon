# 7-segment representation for each digit from 0 to 9
digit = {
    '0': "1110111", 
    '1': "0010010",   
    '2': "1011101",   
    '3': "1011011",   
    '4': "0111010",   
    '5': "1101011",   
    '6': "1101111",   
    '7': "1010010",   
    '8': "1111111",   
    '9': "1111011"
}

# 몇 개 다른지 계산하는 함수
def count_differences(d1, d2):
    return sum(1 for a, b in zip(d1, d2) if a != b)

# 숫자를 7-segment 디스플레이 형식으로 변환하는 함수
def get_digit_represent(num, K):
    num_str = str(num)
    fixed_str = "0" * (K - len(num_str)) + num_str
    return [digit[i] for i in fixed_str]

# 가능한 층수를 계산하는 함수
def calculate_possible_floors(X, N, K, P):
    X_digit = get_digit_represent(X, K)
    possible_floors = 0

    def backtrack(pos, current_digits, changes):
        nonlocal possible_floors
        if changes > P:
            return
        if pos == K:
            floor_number = int("".join(current_digits))
            if 1 <= floor_number <= N and 1 <= changes <= P:
                possible_floors += 1
            return

        current_digit = X_digit[pos]
        for i in range(10):
            new_digit = str(i)
            if current_digit != new_digit:
                diff = count_differences(current_digit, digit[new_digit])
                current_digits[pos] = new_digit
                backtrack(pos + 1, current_digits, changes + diff)
                current_digits[pos] = current_digit
            else:
                backtrack(pos + 1, current_digits, changes)

    backtrack(0, list(X_digit), 0)
    return possible_floors

# 입력 받기
n, k, p, x = map(int, input().split())

# 가능한 층수의 개수 출력
print(calculate_possible_floors(x, n, k, p))
