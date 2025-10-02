from collections import deque
def solution(n, t, m, timetable):
    answer = ''
    # n은 횟수
    # t는 운행 간격(time)
    # m은 최대 인원수 (1회)
    def to_minutes(time):
        h, m = map(int, time.split(':'))
        return h*60 + m 
    
    def to_hours(minute):
        h = minute // 60
        m = minute % 60
        return f"{h:02d}:{m:02d}"
       
    times = deque(sorted(to_minutes(time) for time in timetable))
    
    bus_time = 9 * 60
    
    for i in range(n):
        cnt = 0
        while times and times[0] <= bus_time and cnt < m:
            last = times.popleft()
            cnt += 1
        
        # 마지막 셔틀인 경우
        if i == n -1:
            if cnt < m:
                return to_hours(bus_time)
            else:
                return to_hours(last-1)

        bus_time += t  
        
        