
def sol():
    S = input()
    T = input()
    n = len(T)

    # A 추가
    def minus_A(string):
        return string[:-1]
        
    # B 추가 후 뒤집기
    def minus_B(string):
        s = string[1:]
        return s[::-1]
    
    cnt = 0
    def check(string):
        if string == S:
            return 1
        if len(string) < len(S):
            return 0
        
        res = 0
        if string[-1] == 'A':
            res = res or check(minus_A(string))
        if string[0] == 'B':
            res = res or check(minus_B(string))
        
        return res

    print(check(T))

    return

sol()