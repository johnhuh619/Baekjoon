n = int(input())
# 1*2 / 2*1 / 2*2
# 2 / 1 / 1
# n1 = a
# n2 = c / 2b / 2a
# n3 = (3a) / (c) + (a) / (2b) + (a) / a + c / a + 2b
# n4 = ()

# dp[n] = dp[n-1] + dp[n-2] * 2     


if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    b, a = 3, 1
    for _ in range(3,n+1):
        b, a = (b + a*2)%10007 , b
    print(b)