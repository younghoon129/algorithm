import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\baekjoon\\251030_BAEK10157_자리배정\\BAEK_10157_input.txt', 'r')
from pprint import pprint
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

n, m = map(int, input().split())  # 가로, 세로 (7, 6)
num = int(input())
box = [[0] * m for _ in range(n)]
cnt = 1
i, j = 0, 0
t = 0
box[i][j] = 1
result = 0
if n*m < num:
    print(0)
    exit()
while cnt < n*m:
    k = t%4

    nx, ny = i+dx[k], j+dy[k]
    if 0 <= nx < n and 0 <= ny < m:  # n=7, m=6
        if box[nx][ny]:
            # print('@@@@@@@@@@@@@@@@@')
            t += 1
            continue
        cnt += 1        
        box[nx][ny] = cnt
        i, j = nx, ny
    else:
        # print('!!!!!!!!!!!!!!1', t, k)
        t += 1
        continue
    
    # print(cnt)
    # print(i, j)
    if cnt == num:
        result = [i+1, j+1]
if result:
    print(*result)
else:
    print(result)