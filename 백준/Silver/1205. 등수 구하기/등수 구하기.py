# 입력 조건
# P 리스트에 올라갈 점수 개수
# N 리스트에 있는 점수 개수
# 0 <= N < P
# new_score 리스트 에서 몇등?
# 로직
# 그냥 바로 삽입 후 리스트 정렬
# P 로 리스트 길이 알기 때문
# 리스트 가장 뒤에 new값이 있는지 없는지 추가적으로 확인

N, new_score, P = list(map(int, input().split()))
if N:
    score = list(map(int, input().split()))
    score.append(new_score)
    score.sort(reverse=True)
    idx = score.index(new_score) + 1
    # length가 P 넘어갈 경우
    if idx > P:
        print(-1)
    else:
        # full 이면 new가 기존의 가장 작은 수보다 커야 들어갈 수 있다.
        # 그러므로 가장 작은 수와 new가 일치하면 안 들어갔다고 볼 수 있음.
        if N == P and new_score == score[-1]:
            print(-1)
        else:
            print(idx)
else:
    print(1)
