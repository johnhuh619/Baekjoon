def solution(numLog):
    ans= ""
    for i in range(1,len(numLog)):
        diff = numLog[i] - numLog[i-1]
        if diff == 1:
            ans += "w"
        elif diff == -1:
            ans += "s"
        elif diff == 10:
            ans += "d"
        elif diff == -10:
            ans += "a"
    return ans