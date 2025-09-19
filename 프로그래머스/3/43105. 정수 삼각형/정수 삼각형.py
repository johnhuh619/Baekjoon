def solution(triangle):
    depth = len(triangle) -1 
    while depth >0:
        for i in range(depth):
            triangle[depth-1][i] += max(triangle[depth][i], triangle[depth][i+1])
        depth -= 1
    return triangle[0][0]

# 이동 규칙
# cur_idx 기준 => cur_idx & cur_idx + 1