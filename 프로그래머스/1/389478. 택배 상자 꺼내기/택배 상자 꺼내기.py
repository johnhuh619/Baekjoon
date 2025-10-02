def solution(n, w, num):
    answer = 1
    row = (num -1) // w
    col = (num -1 ) % w
    
    if row % 2 == 1:
        col = w -1 -col
    
    answer = 1
    full_rows = n // w         # 꽉 찬 줄 개수
    rest = n % w               # 마지막 줄의 남은 상자 개수
    total_rows = full_rows if rest == 0 else full_rows + 1  # 총 줄 개수
    
    for r in range(row + 1, total_rows):
        if r < full_rows:
            length = w
        else:
            length = rest if rest != 0 else w
        
        if r % 2 == 0:
            if col < length:
                answer += 1
        else:
            if w - 1 -col < length:
                answer += 1
        
    return answer