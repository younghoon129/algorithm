# 17:05 ~ 17:20

n = [list(map(int, input().split())) for _ in range(4)]

box = [[0]*101 for _ in range(101)]
cnt = 0
for y1, h1, y2, h2 in n:

    for i in range(h2-h1):
        for j in range(y2-y1):
            if box[i+h1][j+y1] == 0:
                cnt += 1
            box[i+h1][j+y1] = 1
print(cnt)

