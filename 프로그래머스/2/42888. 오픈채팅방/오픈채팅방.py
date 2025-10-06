from collections import defaultdict
def simulator(record):
    rec = []
    match = {}
    for data in record:
        parts = data.split()
        act = parts[0]
        uid = parts[1]
        
        if act == "Enter":
            name = parts[2]
            match[uid] = name
            rec.append((act, uid))
        elif act == "Leave":
            rec.append((act, uid))
        else:
            name = parts[2]
            match[uid] = name
    return rec, match

def solution(record):
    answer = []
    rec, match = simulator(record)
    for act, uid in rec:
        if act == "Enter":
            answer.append(f"{match[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{match[uid]}님이 나갔습니다.")
    return answer