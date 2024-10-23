
def solution(numbers):
    numbers.sort()
    number_dict = {}
    for num in numbers:
        for i in range(1, len(num)+1):
            prefix = num[:i]
            if prefix in number_dict:
                return "NO"
        number_dict[num] = True    
    return "YES"

numbers = []
t = int(input())

for _ in range(t):
    n = int(input())
    for _ in range(n):
        numbers.append(input())
    print(solution(numbers))
    numbers.clear()