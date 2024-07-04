def solution(numbers, n):
    current_sum = 0
    for i in numbers:
        if current_sum > n:
            return current_sum
        current_sum += i
    return current_sum