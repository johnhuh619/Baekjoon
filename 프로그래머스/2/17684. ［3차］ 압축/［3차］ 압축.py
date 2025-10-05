def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(ord('A') + i)] = i + 1
    
    temp = ''
    cnt = 26

    for ch in msg:
        temp += ch
        if temp not in dic:
            cnt += 1
            dic[temp] = cnt
            answer.append(dic[temp[:-1]])
            temp = ch
            
    if temp in dic:
        answer.append(dic[temp])
        
    return answer