def solution(num_list):
    odd_str = ''.join(str(num) for num in num_list if num % 2 != 0)
    even_str = ''.join(str(num) for num in num_list if num % 2 == 0)
    result = int(odd_str) + int(even_str)
    return result