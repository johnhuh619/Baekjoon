def solution(msg):
    dic = { chr(ord('A') + i): i+1 for i in range(26)}
    ans = []
    idx = 26
    i = 0
    while i < len(msg):
        nxt = i + 1
        while nxt <= len(msg) and msg[i:nxt] in dic:
            nxt += 1
        ans.append(dic[msg[i:nxt - 1]])
        if nxt <= len(msg):
            idx += 1
            dic[msg[i:nxt]] = idx
        i = nxt - 1
        
    return ans