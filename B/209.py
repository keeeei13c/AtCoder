N,X = map(int,input().split())
A = list(map(int,input().split()))
# リストの中身を偶数と奇数に分ける
odd = A[0::2]
even = A[1::2]
# 偶数のリストの中身をすべて-1
n = [i - 1 for i in even]
#偶数のリスト(-1された)と奇数を合計
total = sum(odd + n)

if X >= total:
    print('Yes')
else: 
    print('No')





   