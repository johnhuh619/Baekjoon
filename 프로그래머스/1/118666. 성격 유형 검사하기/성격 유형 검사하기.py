def simulator(dic, c, suv):
    score = dic[str(c)]
    if score < 0:
        return (suv[0], abs(score))
    elif score == 0:
        return (0, 0)
    else:
        return (suv[1], score)
        
    
def solution(survey, choices):
    dic = {
        "7" : 3,
        "6" : 2,
        "5" : 1,
        "4" : 0,
        "3" : -1,
        "2" : -2,
        "1" : -3
    }
    
    res = {}
    for i, c in enumerate(choices):
        typ, point = simulator(dic, c, survey[i])
        if typ not in res:
            res[typ] = point
        else:
            res[typ] += point
    
    answer = ''
    if res.get("R", 0) >= res.get("T",0):
        answer+= "R"
    else:
        answer+= "T"

    if res.get("C", 0) >= res.get("F", 0):
        answer += "C"
    else:
        answer += "F"

    if res.get("J", 0) >= res.get("M", 0):
        answer += "J"
    else:
        answer += "M"

    if res.get("A", 0) >= res.get("N", 0):
        answer += "A"
    else:
        answer += "N"
    
    return answer