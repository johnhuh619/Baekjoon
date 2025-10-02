from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    target = (s1 + s2) // 2
    
    limit = (len(q1) + len(q2))*4
    
    answer = 0
    
    while answer <= limit:
        
        if s1 == s2:
            return answer
        if s1 < target:
            t = q2.popleft()
            q1.append(t)
            s1 += t
            s2 -= t
        else:
            t = q1.popleft()
            q2.append(t)
            s1 -= t
            s2 += t
        answer += 1
            
    return -1