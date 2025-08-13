from collections import deque

def solution(begin, target, words):
    
    def diff(x, y):
        diff = 0
        for i in range(len(y)):
            if x[i] != y[i]:
                diff += 1
        return diff
    
    
    q = deque([(begin,0)])
    visited = [False]*len(words)
    while q:
        word, dist = q.popleft()
        if word == target:
            return dist
        
        for i in range(len(words)):
            if diff(word, words[i]) == 1 and not visited[i]:
                visited[i] = True
                dist += 1
                q.append((words[i], dist))
    return 0