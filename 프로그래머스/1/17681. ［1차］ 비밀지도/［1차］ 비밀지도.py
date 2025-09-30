def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        r1 = format(arr1[i], f"0{n}b")
        r2 = format(arr2[i], f"0{n}b")
        t = ''
        for j in range(n):
            if r1[j] == '1' or r2[j] == '1':
                t+='#'
            else:
                t+=' '
        answer.append(t)
    return answer