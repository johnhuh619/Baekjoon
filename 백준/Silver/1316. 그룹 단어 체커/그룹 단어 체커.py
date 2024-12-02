import sys
N = int(input())
vocab = [sys.stdin.readline().rstrip() for _ in range(N)]
cnt = 0

def sol(word):
    check = set()
    prev_char = ''
    for char in word:
        if char != prev_char:
            if char in check:
                return 0
            check.add(char)
        prev_char = char
    return 1

for word in vocab:
    if sol(word):
        cnt+=1
print(cnt)

