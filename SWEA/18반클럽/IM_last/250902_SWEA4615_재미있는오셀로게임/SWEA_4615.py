# 14:23 : 14:19 - 2
dxy = [[1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())  # 박스칸, 돌 놓는 횟수
    box = [[0]*n for _ in range(n)]
    a = (n//2)-1
    box[a][a] = 2
    box[a][a+1] = 1
    box[a+1][a] = 1
    box[a+1][a+1] = 2
    for mm in range(m):
        yy, hh, rock = map(int, input().split())  # rock 1(흑) rock 2(백)
        y = yy-1
        h = hh-1
        box[h][y] = rock
        for dx, dy in dxy:
            nx = h + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if rock == box[nx][ny]:
                    continue


                elif rock != box[nx][ny]:            
                    for k in range(1, n):  # 돌 바꾸기
                        if 0 <= nx*k < n and 0 <= ny*k < n:
                            if box[nx*k][ny*k] == rock:


                                for q in range(k+1):
                                    print(q, box[nx*q][ny*q], '123wqasdas')
                                    box[nx*q][ny*q] = rock
    
    # print(sum([i.count(1) for i in box]))
    # print(sum([i.count(2) for i in box]))
    # max_rock = max(black, white)
    print(box)