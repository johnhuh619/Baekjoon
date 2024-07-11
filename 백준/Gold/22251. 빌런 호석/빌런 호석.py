# 무작위로 바꿔서 지정해 놓은 숫자 묶음과 비교.
digit = {
    '0': "11101111", 
    '1':"0010010",   
    '2':"1011101",   
    '3':"1011011",   
    '4':"0111010",   
    '5':"1101011",   
    '6':"1101111",   
    '7':"1010010",   
    '8':"1111111",   
    '9':"1111011"    
}

# 몇개 다른지
def count_differences(d1,d2):
    return sum(1 for a,b in zip(d1,d2) if a!=b)

def get_digit_represent(num,K):
    num_str = str(num)
    fixed_str = "0" * (K - len(num_str)) + num_str
    return [digit[i] for i in fixed_str]
# 1670
# [digit[1], digit[6], digit[7], digit[0]]


# x -> 실제 층
# n -> 층의 최댓값
# k -> 자릿수
# p -> 반전 개수
def calculate_possible_floors(X, N, K, P):
    X_digit = get_digit_represent(X,K)

    possible_floor = []
    for floor in range(1,N+1):
        floor_digit = get_digit_represent(floor,K)

        total_change = sum(count_differences(d1,d2) for d1, d2 in zip(X_digit,floor_digit))
        
        if 1 <= total_change <= P:
            possible_floor.append(floor)
    return possible_floor


n,k,p,x = map(int, input().split())
print(len(calculate_possible_floors(x,n,k,p)))
