n = int(input())
egg = [list(map(int,input().split()))for _ in range(n)]
ans = 0


def hitEgg(depth, egg):
    global ans
    if depth == n:          # 종료조건: depth가 끝에 도달하면 -> 깨진 계란 갯수 세기 
        cnt = 0
        for e in egg:
            if e[0] <= 0:    # 내구 < 0 인지 확인
                cnt+=1
        ans = max(ans,cnt)  # 최대값인지 비교함. 
        return
    if egg[depth][0] <= 0:  # 현재 들고 있는 egg 의 내구 체크
        hitEgg(depth+1,egg)
    else:
        isBroken = True
        for i in range(n):  # 좌축
            if depth != i and egg[i][0] > 0:
                isBroken = False
                egg[depth][0] -= egg[i][1]
                egg[i][0] -= egg[depth][1]
                hitEgg(depth+1,egg)
                egg[depth][0] += egg[i][1]
                egg[i][0] += egg[depth][1]
        if isBroken:
            hitEgg(n,egg)
    
hitEgg(0,egg)
print(ans)