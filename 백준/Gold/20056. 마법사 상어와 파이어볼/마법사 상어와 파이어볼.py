# K 번 반복 => 이동 / 합치기 / 나누기 
def solution(N,M,K,current_field):
    # fireball -> r행/ c열/ 질량/ 속력/ 방향
    # field 에 삽입
    for _ in range(M):
        r, c, m, s, d = map(int,input().split())
        current_field[r-1][c-1].append([m,s,d])

    dir = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

    for _ in range(K):
        move_field = [[[] for _ in range(N)] for _ in range(N)]
        # 2. move_field 활용해 fireball 이동시키기
        for i in range(N):
            for j in range(N):
                if current_field[i][j] != []:
                    for m, s, d in current_field[i][j]:
                        r = (i + dir[d][0] * s) % N
                        c = (j + dir[d][1] * s) % N
                        move_field[r][c].append([m, s, d])

        # 3. 이동한 fireball 확인 & 2개 이상이면 합체    
        for i in range(N):
            for j in range(N):
                if len(move_field[i][j]) >= 2:
                    tmp_m = 0   # 질량
                    tmp_s = 0   # 속력
                    d_odd = 0   # checker
                    d_even = 0
                    for m,s,d in move_field[i][j]:
                        tmp_m += m
                        tmp_s += s
                        if d % 2 == 0: d_even += 1
                        if d % 2 != 0: d_odd += 1

                    # 3-1. 질량은 [(합쳐진 파이어볼 질량의 합)/5] 이다.
                    tmp_m //= 5
                    # 3-4. 질량이 0인 파이어볼은 소멸되어 없어진다.
                    if tmp_m == 0:
                        move_field[i][j] = []
                        continue
                    tmp_len = len(move_field[i][j])    

                    # 3-2. 속력은 [(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)] 이다.
                    tmp_s = tmp_s // tmp_len

                    # fireball 재삽입을 위해 필드 초기화. 
                    move_field[i][j] = []

                    # 3-3. 합쳐지는 파이어볼의 방향의 속성이 같으면 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
                    if d_even == tmp_len or d_odd == tmp_len:
                        for d in [0,2,4,6]:
                            move_field[i][j].append([tmp_m,tmp_s,d])
                    else:
                        for d in [1,3,5,7]:
                            move_field[i][j].append([tmp_m,tmp_s,d])
            current_field = [lst[:] for lst in move_field]

    ans = 0
    for i in range(N):
        for j in range(N):
            if current_field[i][j] != []:
                for m, s, d in current_field[i][j]:
                    ans += m
    return ans

# 1. ipnut

N, M, K = map(int, input().split())
current_field = [[[] for _ in range(N)] for _ in range(N)]
ans = solution(N,M,K,current_field)
print(ans)   
                

