import sys
sys.stdin = open('BAEK_21608_input.txt', 'r')
from pprint import pprint
dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

n = int(input())

student = [list(map(int, input().split())) for _ in range(n*n)]
box = [[0] * n for _ in range(n)]

for s in range(0, len(student)):
    st = student[s][0]
    like_list = student[s][1:]

    max_place = -1
    which = [-1, -1]
    max_like_st = -1
    for i in range(n):
        for j in range(n):
            if box[i][j]: continue

            place = 0
            like_st = 0
            for dx, dy in dxy:
                nx, ny = dx + i, dy + j

                if 0 <= nx < n and 0 <= ny < n:
                    if not box[nx][ny]:
                        place += 1
                    if box[nx][ny] in like_list:
                        like_st += 1
            if like_st > max_like_st:
                max_like_st = like_st
                max_place = place
                which = [i, j]
            elif like_st == max_like_st and place > max_place:
                max_place = place
                which = [i, j]

    box[which[0]][which[1]] = st

total = 0
for i in range(n):
    for j in range(n):
        near_like = 0
        me = box[i][j]
        for l in range(len(student)):
            if me == student[l][0]:
                s_list = student[l][1:]
        for dx, dy in dxy:
            nx, ny = dx + i, dy + j
            if 0 <= nx < n and 0 <= ny < n:
                if box[nx][ny] in s_list:
                    near_like += 1
        if near_like == 1:
            total += 1
        elif near_like == 2:
            total += 10
        elif near_like == 3:
            total += 100
        elif near_like == 4:
            total += 1000
print(total)
# print(box)