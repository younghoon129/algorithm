import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\baekjoon\\251022_BAEK2578_BINGO\\BAEK_2578.txt', 'r')

UD = ((-1, 0), (1, 0))  # 위아래
LR = ((0, 1), (0, -1))  # 좌우
LC = ((-1, -1), (1, 1))  # 왼대
RC = ((-1, 1), (1, -1))  # 오대

def bfs(box):
    pass


n = 5
box = [list(map(int, input().split())) for _ in range(n)]
box_size = n**2
while box_size:
    visited = [[False] * n for _ in range(n)]
    UD_num = 0
    LR_num = 0
    LC_num = 0
    RC_num = 0
    X_num = int(input())
    for i in range(n):
        for j in range(n):
            if X_num == box[i][j]:
                box[i][j] = 0
                bfs(box)


    box_size -= 1


        