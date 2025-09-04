# 00:20 ~ 00:28
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
num = [50000,10000,5000,1000,500,100,50,10]
for t in range(1, test+1):
    n = int(input())
    mon = [0]*8
    for i in range(8):
        mon[i] = n//num[i]
        n %= num[i]
    print(f"#{t}")
    print(' '.join(map(str, mon)))