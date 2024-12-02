tot_grade = 0
tot_point = 0
for _ in range(20):
    name, p, grade = map(str, input().split())
    tmp = 0
    if grade != 'P':         
        tot_grade += float(p)
    if grade == 'A+':
        tmp = 4.5
    elif grade == 'A0':
        tmp = 4.0
    elif grade == 'B+':        
        tmp = 3.5
    elif grade == 'B0':
        tmp = 3.0
    elif grade == 'C+':
        tmp = 2.5
    elif grade == 'C0':
        tmp = 2.0
    elif grade == 'D+':
        tmp = 1.5
    elif grade == 'D0':
        tmp = 1.0
    tot_point += float(p)*tmp
ans = float(tot_point/tot_grade)
print("{:5f}".format(ans))