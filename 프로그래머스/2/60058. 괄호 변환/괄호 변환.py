def is_correct(u):
    stack = []
    for ch in u:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

def split_uv(p):
    cnt = 0
    for i, ch in enumerate(p):
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt == 0:
            return p[:i+1], p[i+1:]
    return p, ""
    
def flip(u):
    result = ''
    for ch in u:
        if ch == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(p):
    answer = ''
    
    if not p:
        return ""
    # 분리    
    u, v = split_uv(p)

    # 검증
    if is_correct(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + flip(u[1:-1])
    
    return answer