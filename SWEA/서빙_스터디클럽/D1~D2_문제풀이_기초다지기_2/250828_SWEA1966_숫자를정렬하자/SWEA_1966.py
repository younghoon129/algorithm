# 00:30 ~ 00:42
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = list(map(int, input().split()))
    a = sorted(box)
    print(f"#{t}",*a)