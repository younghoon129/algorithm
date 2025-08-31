# 02:13 ~ 02:26
# import sys
# sys.stdin = open("C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\IM_last\\250831_SWEA1210_Ladder1\\1210_input.txt", "r")
dxy = [[0,-1], [0, 1], [-1, 0]]

for t in range(1, 11):
    test = int(input())
    box = [list(map(int, input().split())) for _ in range(100)]
    st = 0
    for q in range(100):
        if box[99][q] == 2:
            st = q
            break
    #============================================
    h, y = 99, q
    while h > 0:

        for dx, dy in dxy:
            hx = dx + h
            yy = dy + y
            if 0 <= hx < 100 and 0 <= yy < 100 and box[hx][yy] != 0:
                h = hx
                y = yy
                box[hx][yy] = 0
    print(f"#{t} {y}")