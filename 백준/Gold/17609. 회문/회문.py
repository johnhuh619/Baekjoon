
# 회문 -> 대칭 -> char 의 합이 동일함. 
def is_palindrome(text,left,right):
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

def solution():
    text = input()
    left_end = 0
    right_end = len(text) -1
    while left_end < right_end:
        if text[left_end] == text[right_end]:
            left_end += 1
            right_end -= 1
        else:
            # left <-> right 다른 경우 문자 하나 제거 해보기
            # 먼저 right 제거해보기 (제거 후 합침)
            if is_palindrome(text,left_end+1,right_end) or is_palindrome(text,left_end,right_end-1):
                return 1
            else:
                return 2
    return 0
n = int(input())
for _ in range(n):
    print(solution())