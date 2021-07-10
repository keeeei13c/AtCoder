A,B = map(int,input().split())

ans = B - A
if A < B:
    print(ans+1)
else:
    print(0)