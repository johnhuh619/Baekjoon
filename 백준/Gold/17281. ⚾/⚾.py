N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
# 1. out을 저장한다. 
# 2. while 문으로 타순을 초기화 ex) 1 ... 9 -> 1 이어서 계속
# 3. 이닝 의 변경시에 타자를 저장한다. ex) 1 ...6 -> 7 부터 시작
# 4. 타순은 [0] = 4, [1] ... [8]
players = [i for i in range(1, 9)]
result = float('-inf')

visited = [0] * 9 
def permutations(new_arr, n):
    global players
    if len(new_arr) == n:
        yield new_arr
        return
    for i in range(len(players)):
        if not visited[i]:
            visited[i] = 1
            yield from permutations(new_arr + [players[i]], n)
            visited[i] = 0
    

for x in permutations([], 8):
    batter = x[:3] + [0] + x[3:] # 1번 타자 4번으로 고정
    number, point = 0, 0 # 타순, 점수 초기화

    for i in range(N):
        out = 0
        p1 = p2 = p3 = 0 # 1루, 2루, 3루 주자 상황
        while out < 3:
            if game[i][batter[number]] == 0:
                out += 1
            elif game[i][batter[number]] == 1:
                point += p3
                p1, p2, p3 = 1, p1, p2
            elif game[i][batter[number]] == 2:
                point += p2 + p3
                p1, p2, p3 = 0, 1, p1
            elif game[i][batter[number]] == 3:
                point += p1 + p2 + p3
                p1, p2, p3 = 0, 0, 1
            elif game[i][batter[number]] == 4:
                point += p1 + p2 + p3 + 1
                p1, p2, p3 = 0, 0, 0

            number += 1
            if number == 9:
                number = 0
    result = max(result, point)


print(result)
