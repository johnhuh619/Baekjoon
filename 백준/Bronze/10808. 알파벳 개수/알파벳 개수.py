S = input().strip()

# 알파벳 소문자에 대한 딕셔너리 초기화
alphabet_count = {chr(i): 0 for i in range(97, 123)}

# 각 알파벳의 개수 세기
for char in S:
    alphabet_count[char] += 1

# 결과 출력
print(' '.join(str(alphabet_count[chr(i)]) for i in range(97, 123)))