N = int(input())

# for n in range(N):
bingo = [list(map(str, input().split())) for _ in range(N)]
Max_num = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        x_num = 0
        for k in range(4):
            cnt = 0
            step = 0
            
            if(0 <= i + dx[k] < N and 0 <= j+dy[k] < N and bingo[i][j] == 'O'):
                if(bingo[i+dx[k]][j+dy[k]] == 'X'):
                    Max_num +=1
                    if(0 <= i + dx[k]*l < N and 0 <= j+dy[k]*l < N):
                        if(bingo[i+dx[k]*l][j+dy[k]*l] == 'X'):
                            Max_num +=1
                        elif(bingo[i+dx[k]*l][j+dy[k]*l] == 'O'):
                            break
print(Max_num)