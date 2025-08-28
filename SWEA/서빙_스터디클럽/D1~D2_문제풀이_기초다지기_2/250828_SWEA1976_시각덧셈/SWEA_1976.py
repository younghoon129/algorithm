# # 15:30 ~ 15: 09
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    time = list(map(int, input().split()))
    h = 0
    m = 0
    for ti in range(4):
        if ti%2 == 0:
            h += time[ti]
            if h >= 12:
                h %= 12
        else:
            m += time[ti]
            if m >= 60:
                h += 1
                m %= 60

    print(f"#{t} {h} {m}")