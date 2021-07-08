from math import factorial

P = int(input())

money = [factorial(i) for i in range(10, 0, -1)]
ans = 0
for m in money:
    while m <= P:
        P -= m
        ans+= 1

print(ans)