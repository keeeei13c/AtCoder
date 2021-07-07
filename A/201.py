A1, A2, A3 = map(int, input().split())

z = [A1, A2, A3]
z.sort()

x = z[1] - z[0]
y = z[2] - z[1]

if x == y:
    print('Yes')
else:
    print('No')
