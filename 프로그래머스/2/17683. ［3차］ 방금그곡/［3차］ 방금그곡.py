# 시작 / 끝 / 음악 제목 / 악보정보(회전 큐)
# 음 종류 => 12개
# 음은 분당 1개. 
# 즉, 시간 기준으로 재생된 음악: key / 음악 이름: value => hashmap 에 ㅇ삽입 
# m 과 일치하는지 확인한다. => 해쉬맵에서 서치 O(1)
# 일치하면 value 리턴

# str 시간 -> int 시간 바꾸는 메서드

def convert(m):
    return (m.replace("C#", "c")
            .replace("D#", "d")
            .replace("F#", "f")
            .replace("G#", "g")
            .replace("A#", "a")
            .replace("B#", "b"))

def change(start, end):
    s_hour, s_min = start.split(":")
    e_hour, e_min = end.split(":")
    s = int(s_hour) * 60 + int(s_min)
    e = int(e_hour) * 60 + int(e_min)
    return e - s

# 전체 노래 + 이름 구조의 딕셔너리 생성하는 메서드
def make_track(t, pattern):
    cp = convert(pattern)
    rep = t // len(cp)
    tail = t % len(cp)
    return cp*rep + cp[:tail]
    
# m과 일치하는지 확인하고 일치하는 name 리턴하는 메서드
def solution(m, musicinfos):
    m = convert(m)
    res = []
    for idx, i in enumerate(musicinfos):
        start, end, name, pattern = i.split(",")
        t = change(start, end)
        track = make_track(t, pattern)
        if m in track:
            res.append((t, name, idx))
    if not res:
        return "(None)"
    
    res.sort(key=lambda x: (-x[0], x[2]))
    return res[0][1]

# 조건 일치 음악 여러개 가능. len 긴 음악으로 선택
# 재생 시간 같다면, 먼저 입력된 음악.
# 없으면 None