def solution(players, m, k):
    ans = 0
    active = 0
    off = [0]*(24 + k + 1)
    
    for t in range(24):
        active += off[t]
        expand = players[t] // m
        if active < expand:
            add = expand - active
            ans += add
            active += add
            off[t+k] -= add

    return ans