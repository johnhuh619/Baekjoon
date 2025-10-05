

def solution(id_list, report, k):
    answer = []
    
    # 중복 제거
    report = set(report)
    report_cnt = {user: 0 for user in id_list}
    reporters = {user: [] for user in id_list}
    
    for r in report:
        reporter, target = r.split()
        report_cnt[target] += 1
        reporters[reporter].append(target)
        
    ban = []
    for id, cnt in report_cnt.items():
        if cnt >= k:
            ban.append(id)
    
    for id in id_list:
        m = sum(1 for target in reporters[id] if target in ban)
        answer.append(m)
        
    return answer