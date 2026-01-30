# 1, 2, 3 (규칙 3개 우선순위 존재)
N = int(input())
dic = {}
order = []
for _ in range(N*N):
    data = list(map(int, input().split()))
    dic[data[0]] = data[1:]
    order.append(data[0])

    
room = [[0]*N for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for st in order:
    best_score = (-1, -1, -1, -1) # like, 빈칸, -r, -c
    best_pos = (0, 0)
    
    for r in range(N):
        for c in range(N):
            if room[r][c] != 0:
                continue
            
            like_cnt = 0
            empty_cnt = 0
            
            for d in range(4):
                nr = r + dx[d]
                nc = c + dy[d]
                if 0 <= nr < N and 0 <= nc < N:
                    if room[nr][nc] in dic[st]:
                        like_cnt+=1
                    elif room[nr][nc] == 0:
                        empty_cnt+=1
            
            score = (like_cnt, empty_cnt, -nr, -nc)
            if score > best_score:
                best_score = score  
                best_pos = (r, c)
    
    br, bc = best_pos
    room[br][bc] = st
    
score_table = [0, 1, 10, 100, 1000]
ans = 0
for r in range(N):
    for c in range(N):
        st = room[r][c]
        cnt = 0
        
        for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]
            if 0 <= nr < N and 0 <= nc < N:
                if room[nr][nc] in dic[st]:
                    cnt += 1
        
        ans += score_table[cnt]
        
print(ans) 