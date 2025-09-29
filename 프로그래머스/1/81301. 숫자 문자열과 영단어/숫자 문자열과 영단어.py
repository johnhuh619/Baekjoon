def solution(s):
    res = ''
    dic = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    
    res, st = [], ''
    for ch in s:
        if ch.isdigit():
            res.append(ch)
        else:
            st += ch
            if st in dic:
                res.append(str(dic[st]))
                st = ''
    return int(''.join(res))