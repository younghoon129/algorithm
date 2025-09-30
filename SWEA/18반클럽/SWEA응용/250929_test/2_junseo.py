# 문제2: 스마트 로봇 청소기
import heapq
T = int(input())
for tc in range(1, T + 1):
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    memo = [[float('inf') for _ in range(n)] for _ in range(m)]
    si, sj, di, dj = map(int, input().split())
    memo[si][sj] = 0
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pq = []
    heapq.heappush(pq, (0, si, sj))
    while pq:
        temp_total_w, x, y = heapq.heappop(pq)
        if (x, y) == (di, dj):
            break
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # 다익스트라 직진 최대 거리까지 이동 로직 이후 이동된 nx, ny 좌표를 기준으로 가중치 추가
            cnt = 1
            while 0 <= nx < m and 0 <= ny < n and board[nx][ny] != 1:
                cnt += 1
                nx, ny = x + (dx * cnt), y + (dy * cnt)
            cnt -= 1
            nx, ny = x + (dx * cnt), y + (dy * cnt)
            if cnt == 0:
                continue
            total_w = temp_total_w + cnt
            if memo[nx][ny] > total_w:
                memo[nx][ny] = total_w
                heapq.heappush(pq, (total_w, nx, ny))
    if memo[di][dj] == float('inf'):  # 좌표가 갱신되지 않았다면 갈 수 없는 위치이므로 -1
        result = -1
    else:
        result = memo[di][dj]
    print(f"#{tc} {result}")
    print(memo)