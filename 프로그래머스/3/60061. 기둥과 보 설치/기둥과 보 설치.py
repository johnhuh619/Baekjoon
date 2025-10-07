# 판은 한쪽이 기둥 위 혹은 다른 판과 연결.
# 가능한 구조물 지도 만들기
# 구도가? 




def solution(n, build_frame):
    up = set()
    flat = set()
    # validation
    # 1. (x,y) 에 "|"을 세울 수 있는지 확인 메서드
    def check_up(x,y):
        # 1. 바닥 위
        if y == 0:
            return True
        # 2. 아래가 기둥
        if (x, y-1) in up:
            return True
        # 3. cur_idx 가 보의 양 끝
        if (x-1, y) in flat or (x, y) in flat:
            return True
        return False

    # 2. (x, y) 에 "-" 를 새울 수 있는지 확인 메서드
    def check_flat(x,y):
        # 1. 왼쪽 끝 아래 기둥
        if (x, y-1) in up:
            return True
        # 2. 우측 끝 아래 기둥
        if (x+1, y-1) in up:
            return True
        # 3. 좌측/우측 보가 연결되어 있다면
        if (x-1, y) in flat and (x+1, y) in flat:
            return True
        return False
    # 3. 완성된 구조물이 valid 한지 확인하는 메서드
    def is_valid():
        for x, y in up:
            if not check_up(x, y):
                return False
        for x, y in flat:
            if not check_flat(x, y):
                return False
        return True

    # simulation (명령 처리)
    # build_frame 대로 명령 처리. 최종적으로 구조물 만듬.
    for x, y, mode, act in build_frame:
        if act == 1:
            if mode == 0:
                up.add((x,y))
                if not is_valid():
                    up.remove((x,y))
            else:
                flat.add((x,y))
                if not is_valid():
                    flat.remove((x,y))
        else:
            if mode == 0:
                up.remove((x,y))
                if not is_valid():
                    up.add((x,y))
            else:
                flat.remove((x,y))
                if not is_valid():
                    flat.add((x,y))
    ans = []
    for x, y in up:
        ans.append((x,y,0))
    for x, y in flat:
        ans.append((x,y,1))
    ans.sort(key = lambda x: (x[0], x[1]))
    return ans