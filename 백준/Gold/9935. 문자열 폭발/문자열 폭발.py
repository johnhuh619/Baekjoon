def main():
    s = input().rstrip()
    bomb = input().rstrip()
    stack = []
    b = len(bomb)
    for ch in s:
        stack.append(ch)
        if len(stack) >= b and ch == bomb[-1]:
            if ''.join(stack[-b:]) == bomb:
                for _ in range(b):
                    stack.pop()

    ans = ''.join(stack)
    if ans == '':
        return "FRULA"
    else:
        return ans

print(main())