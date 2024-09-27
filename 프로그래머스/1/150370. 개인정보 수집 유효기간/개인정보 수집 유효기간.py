def solution(today, terms, privacies):
    answer = []
    today = list(map(int,today.split('.')))     # ex) 1999 / 09 / 12 
    terms = {i[0]: int(i[2:])for i in terms}    # list -> dictionary
    today = today[0] * 28 * 12 + today[1] * 28 + today[2]
    for i, pri in enumerate(privacies):
        day, kind = pri.split()
        day = list(map(int,day.split('.')))
        month = terms[kind]
        day = day[0] * 12 * 28 + day[1] * 28 + day[2]-1 + month*28
        if day < today:
            answer.append(i+1)
    return answer