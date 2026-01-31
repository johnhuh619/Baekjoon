arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
word = input()

for w in arr:
    word = word.replace(w, ' ')
ans = len(word)
print(ans)
