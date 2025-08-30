# 01:50 ~ 02:00
test = int(input())
for t in range(1, test+1):
    num, k = map(int, input().split())
    box = list(map(int, input().split()))
    max_cnt = 0
    box.sort()
    for i in range(num):
        cnt = 0
        for j in range(i, num):
            if box[i] <= box[j] <= box[i]+k:
                cnt += 1
            else:
                break
        max_cnt = max(max_cnt, cnt)
    print(f"#{t} {max_cnt}")