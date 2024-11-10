n,m = map(int,input().split())
num_dic = {}
p_dic = {}
for i in range(n):
    p_dic[i+1] = input()
    num_dic[p_dic[i+1]] = (i+1)

for i in range(m):
    target = input()
    if target.isalpha():
        print(num_dic[target])
    else:
        print(p_dic[int(target)])
    



