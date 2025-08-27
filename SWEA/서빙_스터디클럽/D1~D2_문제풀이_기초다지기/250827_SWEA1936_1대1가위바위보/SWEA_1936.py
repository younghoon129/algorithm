# 21 : 59 ~ 22 : 04


n, m = map(int,input().split())
if abs(n-m) == 2:
    if n > m:
        print('B')
    else:
        print('A')
else:
    if n > m:
        print('A')
    else:
        print('B')