grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
tot_grade = 0.0
tot_point = 0.0
for _ in range(20):
    name, p, grade = input().split()
    p = float(p)
    if grade == "P":         
        continue
    tot_grade += p*grade_dict[grade] 
    tot_point += p 
ans = tot_grade/tot_point
print("{:5f}".format(ans))