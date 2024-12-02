import sys

word = sys.stdin.readline().rstrip()
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

cnt = 0
mid = ''
res = ''

for char, count in char_count.items():
    if count % 2 == 1:
        cnt += 1
        mid = char
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

for char in sorted(char_count.keys()):
    res += char *(char_count[char] // 2)

print(res + mid + res[::-1])

