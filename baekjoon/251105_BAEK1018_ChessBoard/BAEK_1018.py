import sys
sys.stdin = open('BAEK_1018_input.txt', 'r')
# from collections import deque
# dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
#
#
# def bfs(cnt, i, j):
#     visited = [[False]*m for _ in range(n)]
#     visited[i][j] = True
#     queue = deque()
#     queue.append([i, j])
#
#     while queue:
#         x, y = queue.popleft()
#     for k in range(i, i+8):
#         for l in range(j, j+8):
#
#             for dx, dy in dxy:
#                 nx, ny = dx+k, dy+l
#                 if i <= nx < i+8 and j <= ny < j+8:
#
#
#
#
#
# n, m = map(int, input().split())
# box = [list(map(int, input())) for _ in range(n)]
# min_cnt = 0
#
#
#
#
# for i in range(n-8):
#     for j in range(m-8):
#         cnt = 0
#         bfs(cnt, i, j)


# 입력 받기
# for qw in range(3):
N, M = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(N)]
min_repaints = float('inf')  # 최솟값을 매우 큰 수로 초기화
# 1. 8x8로 자를 수 있는 모든 시작점을 탐색
# 시작 행은 0부터 N-8까지
for start_row in range(N - 8 + 1):
    # 시작 열은 0부터 M-8까지
    for start_col in range(M - 8 + 1):
        # 2. 'W'로 시작하는 패턴과 'B'로 시작하는 패턴을 기준으로
        #    각각 몇 개를 다시 칠해야 하는지 계산
        count_W_start = 0  # 'W'로 시작할 때 다시 칠할 개수
        count_B_start = 0  # 'B'로 시작할 때 다시 칠할 개수
        # 8x8 영역을 한 칸씩 검사
        for i in range(8):
            for j in range(8):
                # 실제 보드 상의 현재 좌표
                current_row = start_row + i
                current_col = start_col + j
                current_color = board[current_row][current_col]
                # (i+j)의 합이 짝수일 때 (시작 칸과 색이 같아야 함)
                if (i + j) % 2 == 0:
                    # 'W'로 시작하는 패턴 기준
                    if current_color != 'W':
                        count_W_start += 1
                    # 'B'로 시작하는 패턴 기준
                    if current_color != 'B':
                        count_B_start += 1
                # (i+j)의 합이 홀수일 때 (시작 칸과 색이 달라야 함)
                else:
                    # 'W'로 시작하는 패턴 기준
                    if current_color != 'B':
                        count_W_start += 1
                    # 'B'로 시작하는 패턴 기준
                    if current_color != 'W':
                        count_B_start += 1
        # 3. 'W' 시작, 'B' 시작 패턴 중 더 적게 칠하는 횟수를 선택
        current_min = min(count_W_start, count_B_start)
        # 4. 전체 최솟값 갱신
        min_repaints = min(min_repaints, current_min)
# 결과 출력
print(min_repaints)