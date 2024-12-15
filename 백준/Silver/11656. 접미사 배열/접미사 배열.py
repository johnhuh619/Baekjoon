word = input()
word_len = len(word)
res = []
for i in range(0,word_len):
  res.append(word[i:])
res.sort()
for w in res:
  print(w)