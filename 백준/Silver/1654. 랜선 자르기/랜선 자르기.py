# 첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다.
# K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다.
# 그리고 항상 K ≦ N 이다.
# 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다.
# 랜선의 길이는 231-1보다 작거나 같은 자연수이다.

def sol():
    K, N = map(int, input().split())
    ns = [int(input()) for _ in range(K)]
    high = max(ns)
    low = 1
    ans = 0
    def check(mid):
        cnt = 0
        for n in ns:
            cnt += n // mid
        return cnt
        
    while low <= high:
        mid = (low + high) // 2
        cur_k = check(mid)
        if  cur_k >= N:
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans

print(sol())