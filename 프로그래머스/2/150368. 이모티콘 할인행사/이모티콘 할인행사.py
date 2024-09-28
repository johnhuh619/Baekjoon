from collections import deque

def solution(users, emoticons):
    answer = [0, 0] # subscribes, sales
    num = [10,20,30,40]
    n = len(emoticons)
    stack = deque()
    stack.append((0,[]))
    while stack:
        idx, discounts = stack.pop()
        
        if idx == n:
            subscribes = 0
            sales = 0
            for user_discount, user_limit in users:
                tot_cost = 0
                for i in range(n):
                    if discounts[i] >= user_discount:
                        discounted_price = emoticons[i] * (100 - discounts[i]) // 100
                        tot_cost += discounted_price
                if tot_cost >= user_limit:
                    subscribes += 1
                else:
                    sales += tot_cost
            if subscribes > answer[0]:
                answer[0] = subscribes
                answer[1] = sales
            elif subscribes == answer[0] and sales > answer[1]:
                answer[1] = sales
            continue
        
        for discount in [10, 20, 30, 40]:
            new_discounts = discounts + [discount]
            stack.append((idx + 1, new_discounts))
            
    return answer