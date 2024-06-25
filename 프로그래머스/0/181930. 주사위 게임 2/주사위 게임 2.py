def solution(a, b, c):
    s = a + b + c    
    s2 = a**2+b**2+c**2
    cnt = len(set([a,b,c]))
    if cnt == 1:
        return s*s2*(a**3+b**3+c**3)
    elif cnt == 2:
        return s*s2
    else:
        return s