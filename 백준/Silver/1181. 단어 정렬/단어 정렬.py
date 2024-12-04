import sys
input = sys.stdin.readline
N = int(input())
vocab = [input().rstrip() for _ in range(N)]

vocab = set(vocab)
vocab = list(vocab)
vocab.sort()
vocab.sort(key=len)

for v in vocab:
    print(v)

