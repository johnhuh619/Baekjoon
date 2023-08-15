num = int(input())
time = list(map(int,input().split()))

def check_time(a, b):
    y , m = 0 , 0
    
    for i in range(a):
        y += (b[i] // 30 + 1) * 10
        m += (b[i] // 60 + 1) * 15
    if y > m:
            print("M", m)
    elif y == m:
        print("Y M",y)
    else:
        print("Y", y)
check_time(num,time)