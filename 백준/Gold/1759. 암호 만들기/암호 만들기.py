L, C = map(int, input().split())
alp = sorted(input().split())  # 알파벳을 사전 순으로 정렬

def dfs(idx, codes):
    if len(codes) == L:
        v_count = 0  # 자음의 개수
        c_count = 0  # 모음의 개수

        for code in codes:
            if code in 'aeiou':
                c_count += 1  # 모음 개수 증가
            else:
                v_count += 1  # 자음 개수 증가
        if c_count >= 1 and v_count >= 2:  # 모음 1개 이상, 자음 2개 이상
            print("".join(codes))
    else: 
        for i in range(idx, C):
            codes.append(alp[i])  # 문자 추가
            dfs(i + 1, codes)  # i + 1부터 다음 문자 선택
            codes.pop()  # 문자 제거 (백트래킹)

dfs(0, [])
