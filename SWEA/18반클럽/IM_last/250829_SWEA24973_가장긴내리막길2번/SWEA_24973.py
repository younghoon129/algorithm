# 16:30

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    st_num = max(map(max, box))
    sdx = []
    for i in range(n):
        for j in range(n):
            if box[i][j] == st_num:
                sdx.append([i, j])
                print(i,j, box[i][j])

    "======================================================="
    print(sdx)
    for sx, sy in sdx:
        cnt = 1
        h, y = sx, sy
        while True:
            n_num = []
            n_idx = []
            for dx, dy in dxy:
                nx = h + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    n_num.append(box[nx][ny])  # 값 넣기
                    n_idx.append([nx, ny])

            if box[h][y] <= min(n_num):
                break
            elif box[h][y] > min(n_num):
                ndx = n_num.index(min(n_num))  # 가장 작은 값의 인덱스
                h, y = n_idx[ndx]
                cnt+=1
        max_cnt = max(max_cnt, cnt)
        # print(cnt)
    print(f"#{t} {max_cnt}")





    
