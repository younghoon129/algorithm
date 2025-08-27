# 21 : 56 ~ 21 : 58


n, m = map(int,input().split())
for i in range(48):
    if i == 0:
        print(n+m)
    elif i == 1:
        print(n-m)
    elif i == 2:
        print(n*m)
    elif i == 3:
        print(n//m)
