def solution(coin, cards):

    n = len(cards)
    target = n + 1
    
    my_cards = cards[:n//3]
    pending_cards = []
    
    round_cnt = 1
    card_idx = n // 3 # 카드 뭉치 시작 인덱스
    
    while card_idx < n :
        pending_cards.append(cards[card_idx])
        pending_cards.append(cards[card_idx+1])
        card_idx += 2
        
        found = False

        # Case1: coin 소모 0 (카드 버리기) 
        for c in my_cards:
            if target - c in my_cards and c != target-c:
                my_cards.remove(c)
                my_cards.remove(target-c)
                found = True
                break
      
        
        # Case 2: 1장 뽑고 1장 버리고 (coin 1개 이상만 가능)
        if not found and coin >= 1:
            for c in my_cards:
                if (target - c) in pending_cards:
                    my_cards.remove(c)
                    pending_cards.remove(target-c)
                    coin -= 1
                    found = True
                    break    
                
        # Case 3: 2장 뽑기 (coin 2개 이상만 가능)
        if not found and coin >= 2 :     
            pair = None
            for c in pending_cards:
                c2 = target - c
                if c2 in pending_cards and c!=c2:
                    pair = (c, c2)
                    break
            if pair:
                pending_cards.remove(pair[0])
                pending_cards.remove(pair[1])
                coin -= 2
                found = True
                    
        if not found: 
            break
        round_cnt += 1
        
    return round_cnt