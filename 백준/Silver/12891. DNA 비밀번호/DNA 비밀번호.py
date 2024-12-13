s,p = map(int,input().split())
word = input()
dna = list(map(int,input().split()))
dic = {'A': dna[0], 'C': dna[1], 'G': dna[2], 'T': dna[3]}
dic_s = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
cnt = 0

for i in range(s-p+1):
    flag = 1
    if i == 0:
        for j in range(p):
            dic_s[word[j]] += 1
    else:
        dic_s[word[i+p-1]] += 1
        dic_s[word[i-1]] -= 1
        
    for key in 'AGCT':
        if dic_s[key] < dic[key]:
            flag = 0
            break
    if flag:
        cnt += 1

print(cnt)