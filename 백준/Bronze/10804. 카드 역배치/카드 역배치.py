cards = list(range(1,21))

for _ in range(10):
    a, b = map(int,input().split())
    cards[a-1:b] = cards[a-1:b][::-1]
    #  [::-1] 시작 위치 -1 => list 마지막 위치 의미
for card in cards:
    print(card, end=' ')