from collections import defaultdict

def solution(gems):
    n = len(gems)
    kinds = set(gems)          
    k = len(kinds)

    counter = defaultdict(int) 
    end, start = n-1, 0
    left = 0
    
    for right in range(n):
        counter[gems[right]] += 1
        
        while len(counter) == k:
            # 길이 확인 => 현재 길이 vs 기존 최단 길이
            if right - left < end - start:
                end, start = right, left
            
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1

    return [start+1, end+1]
            