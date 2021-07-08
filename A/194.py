A,B = map(int,input().split())

milk = A+B
fat = B

if milk >=15 and fat >= 8:
    print(1)
elif milk >= 10 and fat >= 3:
    print(2)
elif milk >=3:
    print(3)
else:
    print(4)