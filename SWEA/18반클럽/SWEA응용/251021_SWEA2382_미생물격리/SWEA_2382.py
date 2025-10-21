import sys
sys.stdin = open('SWEA_2382_input.txt', 'r')

dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 5 <= n <= 100 셀 크기
# 5 <= k <= 1000 격리 시간
# 1 <= m <= 1000 군집 개수
# 세로, 가로, 미생물 수, 이동 방향 순
# 세로위치(1), 가로위치(1), 미생물 수(7), 이동방향(상)
# 1(상), 2(하), 3(좌), 4(우)

def time(box):
    for _ in range(m):

        for i in range(k):

            for dx, dy in dxy:
                nx, ny = box[i][0][0] + dx, box[i][0][1]+ dy






tc = int(input())
for t in range(1, tc+1):
    n, m ,k = map(int, input().split())
    box = []
    virus = []
    for _ in range(k):
        h, y, v, s = map(int, input().split())
        box.append([h, y, s])
        virus.append(v)
    for _ in range(m):
        time(box)
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