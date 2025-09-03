# 13:48 ~ 13: 45

test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = list(map(int, input().split()))
    max_cnt = 1
    cnt = 1
    for i in range(n-1):
        if box[i] < box[i+1]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    print(f"#{t} {max_cnt}")