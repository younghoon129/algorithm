# # 15:16 ~ 19
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    n = int(input())
    num = 0
    for i in range(1, n+1):
        if i%2 == 0:
            num -= i
        elif i%2 == 1:
            num += i
    print(f"#{t} {num}")