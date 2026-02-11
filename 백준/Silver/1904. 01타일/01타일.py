n = int(input())
# 1 => n-1 
# 00 => n-2

# dp[n] = dp[n-1] + dp[n-2]

# d[3] = d[2] + d[1]
# d[4] = d[3] + d[2]
# d1 = a
# d2 = b
# d3 = (b) + (a)
# d4 = (a+b) + (b)
# d5 = (a+b+b) + (a+b)
# b -> a+b
# a -> b
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a, b = 1, 2
    for _ in range(3, n+1):
        b, a =  (a+b) % 15746, b 
        
    print(b)
