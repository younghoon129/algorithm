import sys
sys.stdin = open('SWEA_2382_input.txt', 'r')
dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 5 <= n <= 100 셀 크기
# 5 <= k <= 1000 격리 시간
# 1 <= m <= 1000 군집 개수
# 세로, 가로, 미생물 수, 이동 방향 순
# 세로위치(1), 가로위치(1), 미생물 수(7), 이동방향(상)
# 1(상), 2(하), 3(좌), 4(우)

def time(board, box):
    for _ in range(m):  # 변경 횟수
        for i in range(k):  # 미생물 갯수
            q = box[i][0]  # 행
            w = box[i][1]  # 열
            e = board[box[i][2][1]]  # 방향
            if e == 1:
                if board[q - 1][w]:
                    board[q - 1][w] += board[q][w]  # virus 합침
                    e = max()
                board[q - 1][w] = board[q][w]
                q -= 1
                board[q][w] = 0

            elif e == 2:
                board[q + 1][w] = board[q][w]
                q += 1

            elif e == 3:
                board[q][w - 1] = board[q][w]
                w -= 1

            elif e == 4:
                board[q][w + 1] = board[q][w]
                w += 1
            # if  e <= 2:

tc = int(input())
for t in range(1, tc+1):
    n, m ,k = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    box = []
    virus = []
    for _ in range(k):
        h, y, v, s = map(int, input().split()) # 세로, 가로, 미생물, 이동방향
        box.append([h, y])
        virus.append([v, s])

    for i in range(k):
        board[box[i][0]][box[i][1]] = virus[i]

    time(board, box)
    # print(box)




# tc = int(input())
# for t in range(1, tc+1):
#     n, m ,k = map(int, input().split())
#     box = [[0] * n for _ in range(n)]
#     virus = 0
#     for _ in range(k):
#         h, y, v, s = map(int, input().split())
#         box[h][y] = [v, s]
#     for _ in range(m):
#         time(box)