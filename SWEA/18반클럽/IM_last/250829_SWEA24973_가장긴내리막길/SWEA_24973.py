dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
import sys
sys.stdin = open("/input.txt", "r")
test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    st = []  # 여기에 시작점 넣을거임
    s = max(map(max, box))

    for q in range(n):
        for p in range(n):
            if box[q][p] == s:
                st.append([q, p])

    max_cnt = 0
    for h, y in st:  # 최대 고도 여러개 돌리는 거
        cnt = 1  # 1부터 시작
        # print(h, y)
        while True:
            nn = []  # 낮은 고도들
            nidx = []  # 값들의 인덱스

            for dx, dy in dxy:  # 4방향 탐색
                hx = dx + h  # 상하
                hy = dy + y  # 좌우
                if 0 <= hx < n and 0 <= hy < n:  # 범위
                    nn.append(box[hx][hy])  # 고도들에 다음 값들 넣고
                    nidx.append([hx, hy])  # 값들 인덱스 넣고

            if box[h][y] <= min(nn):
                break
            else:
                nnn = nn.index(min(nn))  # nn에서 최솟값의 인덱스를 찾음
                h, y = nidx[nnn]  # 그 인덱스의 번호로 h, y 값 가져옴
                cnt += 1  # 방문 횟수 증가
        max_cnt = max(max_cnt, cnt)  # 방문 횟수들 가장 높은 거
    print(f"#{t} {max_cnt}")
