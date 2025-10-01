def solution(str1, str2):
    answer = 0
    a1 = []
    def make_multi(s):
        s = s.lower()
        arr = []
        for i in range(len(s) - 1):
            a, b = s[i], s[i+1]
            if a.isalpha() and b.isalpha():
                arr.append(a+b)
        return arr
    
    a = make_multi(str1)
    b = make_multi(str2)
    
    b_copy = b[:]
    inter = 0
    
    for x in a:
        if x in b_copy:
            inter += 1
            b_copy.remove(x)
    
    union = len(a) + len(b) - inter
    if union == 0:
        return 65536
    return int((inter / union) * 65536)