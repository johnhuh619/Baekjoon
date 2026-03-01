query = input().rstrip()

stack = []

for ch in query:
    stack.append(ch)
    if len(stack) >= 4:
        if stack[-4:] == ['P','P','A','P']:
            for _ in range(4):
                stack.pop()
            stack.append('P')

if stack == ['P']:
    print("PPAP")
else:
    print("NP")

