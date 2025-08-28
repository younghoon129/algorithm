# # 15:03 ~ 15: 09
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for k in range(m):
                for l in range(m):
                    cnt += box[i+k][j+l]
            max_cnt = max(max_cnt, cnt)
    print(f"#{t} {max_cnt}")