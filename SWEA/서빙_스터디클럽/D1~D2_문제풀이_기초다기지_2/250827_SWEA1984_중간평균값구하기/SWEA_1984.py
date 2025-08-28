# # 15:21 ~
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    box = list(map(int, input().split()))
    box = sorted(box)
    res = (sum(box[1:-1])/(len(box)-2))
    print(f"#{t} {res:.0f}")