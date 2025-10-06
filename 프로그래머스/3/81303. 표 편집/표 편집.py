# 삭제시 => 아래 행들 전부 올라옴. q 쓰면 될듯
# 삭제 시 => cur는 다음 행./ cur가 마지막이면 윗행.
# 최근에 삭제된 행 복구하기 => 최근 삭제 행을 담아 놓는다. 


def solution(n, k, cmd):
    answer = ''
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    next[-1] = -1
    removed = []
    alive = ["O"]*n
    cur = k
    
    for c in cmd:
        parts = c.split()
        cd = parts[0]
        
        if cd == "U":
            for _ in range(int(parts[1])):
                cur = prev[cur]
        elif cd == "D":
            for _ in range(int(parts[1])):
                cur = next[cur]
        elif cd == "C":
            removed.append(cur)            
            alive[cur] = "X"
            pn, nn = prev[cur], next[cur]
            if pn != -1:
                next[pn] = nn                
            if nn != -1:
                prev[nn] = pn
            cur = nn if nn != -1 else pn
        elif cd == "Z":
            # 삭제된 노드의 idx 를 활용
            restore = removed.pop()
            alive[restore] = "O"
            pn, nn = prev[restore], next[restore]
            if pn != -1:
                next[pn] = restore    
            if nn != -1:
                prev[nn] = restore
                
    return ''.join(alive)