from collections import deque
variable = input()
def converter(variable):
    stack = deque()
    flag = 0
    if "__" in variable:
        return "Error!"
    
    if variable[0] == "_" or variable[-1] == "_":
        return "Error!"
    
    if '_' in variable:
        for char in variable:
            if char.isupper():
                return "Error!"
            if char == '_':
                flag = 1
            else:
                stack.append(char.upper() if flag == 1 else char)
                flag = 0
    else:
        if variable[0].isupper():
            return "Error!"
        for char in variable:
            if char.isupper():
                stack.append("_")
                stack.append(char.lower())
            else:
                stack.append(char)
    return stack

print(*converter(variable),sep='')