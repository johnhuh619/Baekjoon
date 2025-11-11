# 첫줄에 과일 개수 N
# 2번 줄에 탕후루에 꽂힌 과일 의미하는 N개의 정수 공백으로 주어짐
def sol():
    N = int(input())
    ns = list(map(int, input().split()))
    dic = {}
    left = 0
    max_len = 0
    for right in range(N):
        n = ns[right]
        dic[n] = dic.get(n,0) + 1
        
        while len(dic) > 2:
            ln = ns[left]
            dic[ln] -= 1
            if dic[ln] == 0:
                del dic[ln]
            left += 1
            
        max_len = max(max_len, right - left + 1)    
    return max_len
print(sol())