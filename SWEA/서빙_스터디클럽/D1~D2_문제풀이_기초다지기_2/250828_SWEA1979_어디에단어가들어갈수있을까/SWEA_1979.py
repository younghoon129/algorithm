# # 18:30 ~ 18:40
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        cnt = 0
        cnt2 = 0
        for j in range(n):
            if box[i][j] == 1:
                cnt += 1
            if box[i][j] == 0 or j == n-1:
                if cnt == m:
                    max_cnt += 1
                cnt = 0

        for k in range(n):
            if box[k][i] == 1:
                cnt2 += 1
            if box[k][i] == 0 or k == n-1:
                if cnt2 == m:
                    max_cnt += 1
                cnt2 = 0
    print(f"#{t} {max_cnt}")

