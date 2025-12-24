from collections import defaultdict
def solution(points, routes):
    answer = 0
    
    points_dict = {}
    
    for i, (r,c) in enumerate(points, start = 1):
        points_dict[i] = (r,c)
    visited = defaultdict(int)
    
    def simulate_robot(route):
        nonlocal answer
        time = 0
        r,c = points_dict[route[0]]
        visited[(time,r,c)] += 1
        if visited[(time,r,c)] == 2:
            answer += 1
            
        for i in range(1,len(route)):
            nr, nc = points_dict[route[i]]
            
            while r != nr:
                r += 1 if r < nr else -1
                time += 1
                visited[(time, r, c)] +=1
                if visited[(time, r, c)] == 2:
                    answer += 1
            while c != nc:
                c += 1 if c < nc else -1
                time += 1
                visited[(time, r, c)] += 1
                if visited[(time, r, c)] == 2:
                    answer += 1
                
    for route in routes:
        simulate_robot(route)
        
    
    return answer