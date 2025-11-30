import sys
sys.stdin = open('BAEK_2468_input.txt', 'r')
import pprint
from collections import deque
import copy

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(q, w, box_2):  # 여기서 갯수 세자
    queue = deque()
    queue.append([q, w])
    box_2[q][w] = 0
    while queue:
        x, y = queue.popleft()
        # print(x, y, cnt)
        # pprint.pprint(box)
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                if not box_2[nx][ny]: continue
                box_2[nx][ny] = 0
                queue.append([nx, ny])

n = int(input())  # 배열 크기
box = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0
# max_num = 0
# for p in range(n):
#     max_num = max(box[p])
max_num = max(map(max, box))
for k in range(max_num):
    box_2 = copy.deepcopy(box)
    cnt = 0
    # pprint.pprint(box_2)
    for i in range(n):
        for j in range(n):
            if box_2[i][j] <= k:
                box_2[i][j] = 0
    # print(k)
    # pprint.pprint(box_2)
    for i in range(n):
        for j in range(n):
            if not box_2[i][j]: continue
            bfs(i, j, box_2)
            cnt += 1
            # print('@@@@@@')
    # print(cnt, k)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
#
#
#
#
#
# # 5
# # 6 8 2 6 2
# # 3 2 3 4 6
# # 6 7 3 3 2
# # 7 2 5 3 6
# # 8 9 5 2 7