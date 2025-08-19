
def sol():
    stack = []
    token = input()
    ans = []
    val = {'+': 0, '-': 0, '*':1, '/': 1}
    for c in token:
        if c =='(':
            stack.append(c)
        elif c in "+-*/":
            while stack and stack[-1] != '(' and val[c] <= val[stack[-1]]: 
                ans.append(stack.pop())
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        else:
            # alphabet 이라면
            ans.append(c)
            
    while stack:
        ans.append(stack.pop())
    return ans
ans = sol()
print(''.join(ans))