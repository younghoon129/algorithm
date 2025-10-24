import sys
# sys.stdin = open('SWEA_2382_input.txt', 'r')
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\251021_SWEA2382_미생물격리\\SWEA_2382_input.txt', 'r')
from collections import defaultdict
dxy = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))

tc = int(input())
for t in range(1, tc+1):
    n, m ,k = map(int, input().split())
    bug_dict = defaultdict(list)
    for i in range(k):
        x, y, cnt, d = map(int, input().split())
        bug_dict[i] = [x, y, cnt, d]
    
    dxy_change = [0, 2, 1, 4, 3]

    while m:
        for idx, val in bug_dict.items():
            x, y, cnt, d = val
            nx = x + dxy[d][0]
            ny = y + dxy[d][1]
            val[0] = nx
            val[1] = ny
            if not(0 < nx < n-1 and 0 < ny < n - 1):
                val[3] = dxy_change[d]
                val[2] = cnt // 2
        visited = defaultdict(list)
        for idx, val in bug_dict.items():
            x, y = val[0], val[1]
            visited[(x, y)].append(idx)
        for idx, val in visited.items():
            if len(val) >= 2:
                king_pos = 0
                max_cnt = 0
                for i in val:
                    if max_cnt < bug_dict[i][2]:
                        king_pos = i
                        max_cnt = bug_dict[i][2]
                for i in val:
                    if i != king_pos:
                        bug_dict[king_pos][2] += bug_dict[i][2]
                        del bug_dict[i]
        m -= 1
    ans = 0
    for idx, val in bug_dict.items():
        ans += val[2]
    print(f"#{t} {ans}")