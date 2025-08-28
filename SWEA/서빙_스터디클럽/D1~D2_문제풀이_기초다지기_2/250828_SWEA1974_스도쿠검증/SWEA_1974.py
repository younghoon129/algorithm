# 11:38 ~ 12:06
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    box = [list(map(int, input().split())) for _ in range(9)] # 9*9박스
    cnt = 1
    for i in range(9):
        h = [0]*10
        y = [0]*10
        for j in range(9):  # 세로 검사
            # print(j, i)
            h[box[j][i]] += 1
            if h[box[j][i]] != 1:
                cnt = 0
                break
        for j in range(9):
            y[box[i][j]] += 1
            if y[box[i][j]] != 1:
                cnt = 0
                break
        for k in range(9):
            if i%3 == 0 and k%3 == 0:
                b = [0]*10
                for l in range(3):
                    for o in range(3):
                        b[box[i+l][k+o]] += 1
                        if b[box[i+l][k+o]] != 1:
                            cnt = 0
                            break
                    if cnt == 0:
                        break
            if cnt == 0:
                break
        if cnt == 0:
            break
    print(f"#{t} {cnt}")