# 00:30 ~ 00:42
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    box_90 = list(map(list, zip(*box[::-1])))
    box_180 = list(map(list, zip(*box_90[::-1])))
    box_270 = list(map(list, zip(*box)))[::-1]
    print(f"#{t}")
    for i in range(n):
        print(''.join(map(str, box_90[i])), end = ' ')
        print(''.join(map(str, box_180[i])), end = ' ')
        print(''.join(map(str, box_270[i])))
