import sys

input = sys.stdin.readline

s = input().rstrip()

ans = []
stack = []
in_tag = False
for ch in s:
    if ch == '<':
        while stack:
            ans.append(stack.pop())
        in_tag = True
        ans.append(ch)
    
    elif ch == '>':
        in_tag = False
        ans.append(ch)
        
    elif in_tag:
        ans.append(ch)
    
    else:
        if ch == ' ':
            while stack:
                ans.append(stack.pop())
            ans.append(ch)
        else:
            stack.append(ch)

while stack:
    ans.append(stack.pop())
    
print(''.join(ans))