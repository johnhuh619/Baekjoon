import sys
n = int(input())
A = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(input())
B = list(map(int,sys.stdin.readline().rstrip().split()))
answer = []
while True:
    sortA = sorted(A, reverse=True)
    maxA = 0    # 1 <=
    for i in sortA:
        if i in B:
            maxA = i    
            break   # max값 한개만 쓰기 위함.
    
    if maxA == 0:
        break
    
    answer.append(maxA)
    nextA_idx = A.index(maxA)
    nextB_idx = B.index(maxA)
    A = A[nextA_idx+1:]
    B = B[nextB_idx+1:]

print(len(answer))
print(*answer)    

    
    
