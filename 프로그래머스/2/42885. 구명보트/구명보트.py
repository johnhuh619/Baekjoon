def solution(people, limit):
    two_p_boat = 0
    # limit 맞추기
    l_p = len(people)
    f = 0
    r = l_p - 1
    people.sort()
    while f < r:
        if people[f] + people[r] <= limit:
            f += 1
            two_p_boat += 1
        r -= 1 
    return l_p - two_p_boat