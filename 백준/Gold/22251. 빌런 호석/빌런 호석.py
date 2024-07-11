# 무작위로 바꿔서 지정해 놓은 숫자 묶음과 비교.
digit = {
    '0': "1110111", 
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
    possible_floor = 0

    def backtrack(pos,current_digits,change):
        nonlocal possible_floor
        if change > P:
            return
        
        if pos == K:
            floor_number = int("".join(current_digits))       
            if 1<= floor_number <= N and 1<= change <= P:
                possible_floor += 1
            return
        
        current_digit = X_digit[pos]
        for i in range(10):
            new_digit = str(i)
            if current_digit != new_digit:
                diff = count_differences(current_digit, digit[new_digit])
                current_digits[pos] = new_digit
                backtrack(pos+1, current_digits, change+diff)
                current_digits[pos] = current_digit
            else:
                backtrack(pos+1, current_digits, change)

    
    backtrack(0,list(X_digit),0)
    return possible_floor


n,k,p,x = map(int, input().split())
print(calculate_possible_floors(x,n,k,p))