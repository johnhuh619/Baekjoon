def to_min(t):
    h, m = map(int,t.split(":"))
    return h*60 + m

def solution(fees, records):
    base_t, base_f, unit_t, unit_f = fees
    in_time = {}
    tot_time = {}
    
    for r in records:
        time, car, mode = r.split()
        m = to_min(time)
        
        if mode == "IN":
            in_time[car] = m
        else:
            tot_time[car] = tot_time.get(car, 0) + m - in_time[car]
            del in_time[car]

    # 출차 23:59 처리
    for car, t in in_time.items():
        tot_time[car] = tot_time.get(car, 0) + (23*60 + 59) - t
    
    answer = []
    for car in sorted(tot_time.keys()):
        t = tot_time[car]
        if t <= base_t:
            res = base_f
        else:
            res = base_f + ((t - base_t + unit_t -1) // unit_t) * unit_f
        answer.append(res)
        
    return answer