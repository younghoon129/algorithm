# 13:17 ~ 13: 45
dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = [list(map(str, input())) for _ in range(n)]
    # print(box[0][1])
    for i in range(n):
        for j in range(n):
            
            for dx, dy in dxy:
                cnt = 0
                for k in range(5):
                    nx = i + dx*k
                    ny = j + dy*k
                    # print(nx, ny,'=====')
                    if 0 <= nx < n and 0 <= ny < n:
                        if box[nx][ny] == 'o':
                            cnt+=1
                        elif box[nx][ny] != 'o':
                            break
                if cnt == 5:
                    break
            if cnt == 5:
                break
        if cnt == 5:
            break
    if cnt == 5:
        print(f"#{t} YES")
    elif cnt != 5:
        print(f"#{t} NO")

    