# 11:38 ~ 11:34
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ddd = [[-1, 1], [1, 1], [1, -1], [-1, -1]]

test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            cnt = [box[i][j], box[i][j]]

            for mu in range(1, m):
                for dx, dy in dxy:
                    nx = i + dx*mu
                    ny = j + dy*mu
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt[0] += box[nx][ny]

                for ddx, ddy in ddd:
                    nnx = i + ddx*mu
                    nny = j + ddy*mu
                    if 0 <= nnx < n and 0 <= nny < n:
                        cnt[1] += box[nnx][nny]
                
            max_cnt = max(max_cnt, max(cnt))
    print(f"#{t} {max_cnt}")