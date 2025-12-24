def solution(diffs, times, limit):
    answer = 0
    def simulator(level):
        
        time_cnt = 0
        
        for i in range(len(diffs)):
            time_prev = times[i-1] if i != 0 else 0
            
            # 1트
            if diffs[i] <= level:
                time_cnt += times[i]
                
            # N트
            else:
                time_cnt += times[i] + (times[i] + time_prev) * (diffs[i] - level)
            
            # 시간 초과
            if time_cnt > limit:
                return False
        
        return True
    
    top, down = max(diffs), 1
    level = top
    while top >= down:
        mid = (top + down) // 2
        if simulator(mid):
            level = mid
            top = mid - 1 
        else:
            down = mid + 1
    
    return level


