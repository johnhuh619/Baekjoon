def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    sets = [set(map(int, x.split(","))) for x in s]
    sets.sort(key=len)
    
    for s in sets:
        num = (s - set(answer)).pop()
        answer.append(num)
    return answer