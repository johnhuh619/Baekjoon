# 1 <= user_id <= 8
# user_id 의 원소 값은 1<= 값 <=8
# banned도 동일
# banned는 * 포함.

# 1. banned_id 길이 비교
# 2. banned_id 의 ch 하나씩 비교
# 3. 가능하다면 배열에 추가. 
# 4. match 한 케이스 를 이용한 dfs.
def solution(user_id, banned_id):
    
    def match(ban, user):
        if len(ban) != len(user):                
            return False
        for i in range(len(ban)):
            if ban[i] != '*' and user[i] != ban[i]:
                return False
        return True
    
    can = []
    
    for ban in banned_id:
        t_can = []
        for u in user_id:
            if match(ban, u):
                t_can.append(u)
        can.append(t_can)
    
    res = set()
    
    # (0, [])
    def dfs(idx, targets):
        if idx == len(banned_id):
            res.add(tuple(sorted(targets)))
            return
        
        for u in can[idx]:
            if u not in targets:
                targets.append(u)
                dfs(idx + 1 ,targets)
                targets.pop()
                
    dfs(0, [])
    answer = len(res)
    return answer