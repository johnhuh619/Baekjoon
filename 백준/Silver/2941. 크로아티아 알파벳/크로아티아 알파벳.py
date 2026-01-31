arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
word = input()

for w in arr:
    while word.find(w) > -1:
        word = word.replace(w, ' ')
ans = len(word)
print(ans)
