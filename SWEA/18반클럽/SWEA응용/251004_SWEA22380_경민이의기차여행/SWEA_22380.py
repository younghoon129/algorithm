import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\251004_SWEA22380_경민이의기차여행\\SWEA_22380_input.txt', 'r')
import heapq
from collections import defaultdict
def bfs(arr, st):
    visited = {v : float('INF') for v in range(n)}
    visited[0] = st
    queue = []
    heapq.heappush(queue, (0, 0))

    while queue:
        dis, move = heapq.heappop(queue)
        if visited[move] < dis: continue

        for idx, num in arr[move].items():
            now_distance = dis + num
            if now_distance < visited[idx]:
                visited[idx] = now_distance
                heapq.heappush(queue, (now_distance, idx))
    if visited[n-1] != float('inf'):
        print(f"#{t} {visited[n-1]}")
    else:
        print(f"#{t} impossible")    

tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    p_list = defaultdict()
    p_list = {v: {} for v in range(n)}
    for i in range(m):
        a, b, w = map(int, input().split())
        p_list[a].update({b : w})
    s_num = 0
    bfs(p_list, s_num)