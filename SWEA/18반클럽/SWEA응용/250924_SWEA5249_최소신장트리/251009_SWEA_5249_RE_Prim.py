import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250924_SWEA5249_최소신장트리\\SWEA_5249_input.txt', 'r')
from collections import defaultdict
import heapq

def prim(vertices, edges):
    global cnt
    mst = []

    adj_list = {v: [] for v in vertices}
    for start_v, end_v, w in edges:
        adj_list[start_v].append((end_v, w))
        adj_list[end_v].append((start_v, w))
    
    visited = set()
    init_vertex = vertices[0]
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]
    heapq.heapify(min_heap)
    visited.add(init_vertex)

    while min_heap:
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited: continue

        visited.add(end_v)
        mst.append((start_v, end_v, weight))
        # print((start_v, end_v, weight))
        cnt += weight
        for adj_v, adj_w in adj_list[end_v]:
            # print(adj_v, end_v, '@@')
            if adj_v in visited: continue
            
            heapq.heappush(min_heap, [adj_w, end_v, adj_v])
    return cnt

tc = int(input())

for t in range(1, tc+1):
    a, b = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(b)]
    vertices = list(range(a+1))
    # print(vertices, edges)
    cnt = 0
    # print(prim(vertices, edges))
    print(f"#{t} {prim(vertices, edges)}")
    # print(f"#{t} {cnt}")