
def simulator(cols, moves):
    ans = []
    cnt = 0
    for m in moves:
        if not cols[m]:
            continue
        n = cols[m].pop()
        if ans and ans[-1] == n:
            cnt += 2
            ans.pop()
            continue
        ans.append(n)
    return cnt

def solution(board, moves):
    N = len(board)
    cols = [[] for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if board[i][j] != 0:
                cols[j+1].append(board[i][j])
    ans = simulator(cols, moves)
                
    return ans