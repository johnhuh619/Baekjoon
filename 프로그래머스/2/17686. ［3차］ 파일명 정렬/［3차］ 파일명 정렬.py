def spliter(file):
    for i, ch in enumerate(file):
        if ch.isdecimal():
            j = i
            while j < len(file) and file[j].isdecimal():
                j+=1
            head = file[:i]
            num = file[i:j]
            tail = file[j:]
            return (head, num, tail)

def solution(files):
    ans = [spliter(f) for f in files]
    ans.sort(key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(map(str, x)) for x in ans]