def solution(num_list, n):
    rear = num_list[n:]+num_list[:n]
    
    return rear