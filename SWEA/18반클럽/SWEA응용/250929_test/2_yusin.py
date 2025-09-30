# import sys
# sys.stdin = open("algo2_sample_in.txt", 'r')
import heapq
T = int(input())
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    sx, sy, ex, ey = map(int, input().split())
    # 얼리 리턴 = 목표지점이 도착할 수 없는 구조하면 즉시 종료
    for dx, dy in dxy:
        nex, ney = ex + dx, ey + dy
        # 목표지점 4방향 중 보드의 끝 or 장애물이 없다면 도착 불가
        if not(0 <= nex < N and 0 <= ney < N) or board[nex][ney] == 1:
            break
    else:
        print(f"#{tc} -1")
        continue
    # 방향별 dist memo
    visi = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    hq = []
    # hq에 시작점 기준 4방향 추가
    for i in range(4):
        # 이동거리, x좌표, y좌표, 방향
        heapq.heappush(hq, (0, sx, sy, i))
        visi[sx][sy][i] = 0
    # 메인루프 시작
    while hq:
        dist, x, y, d = heapq.heappop(hq)
        if visi[x][y][d] > dist:
            continue
        if x == ex and y == ey:
            print(f"#{tc} {dist}")
            break
        # 맵을 벗어나거나 장애물이 나올 때 까지 델타탐색 진행
        # 델타탐색하며 add_move로 이동 횟수 저장
        for idx, (dx, dy) in enumerate(dxy):
            cx, cy = x, y
            add_move = 0
            while True:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 1:
                    break
                add_move += 1
                cx, cy = nx, ny
            nxt_dist = dist + add_move
            # 좌표와 이동방향까지 고려한 dist memo 확인
            if visi[cx][cy][idx] <= nxt_dist:
                continue
            visi[cx][cy][idx] = nxt_dist
            heapq.heappush(hq, (nxt_dist, cx, cy, idx))
    # while문이 정상적으로 끝난것은 도착지점 도착하지 못했다는 것으로 -1 출력
    else:
        print(f"#{tc} -1")
# 100 * 100 * 4 메모리 부담 전혀 없음