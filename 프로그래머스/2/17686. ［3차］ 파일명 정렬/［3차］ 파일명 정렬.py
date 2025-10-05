def spliter(file):
    for i in range(len(file)):
        if file[i].isdecimal():
            head = file[:i]
            j = i
            while j < len(file) and file[j].isdecimal() == True:
                j+=1
            num = file[i:j]
            tail = file[j:]
            return (head, num, tail)

def solution(files):
    ans = [spliter(f) for f in files]
    ans.sort(key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(map(str, x)) for x in ans]