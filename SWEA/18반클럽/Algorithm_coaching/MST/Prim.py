import heapq

def prim(vertices, edges):
    mst = []

    adj_list = {v : [] for v in vertices}
    for s_v, e_v, w in edges:
        adj_list[s_v].append((e_v, w))
        adj_list[e_v].append((s_v, w))

    visited = set()
    init_vertex = vertices[0]
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]
    heapq.heapify(min_heap)
    visited.add(init_vertex)

    while min_heap:
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited:
            continue
        visited.add(end_v)
        mst.append((start_v, end_v, weight))

        for adj_v, adj_w in adj_list[end_v]:
            if adj_v in visited: continue
            heapq.heappush(min_heap, [adj_w, end_v, start_v])
    return mst    
        
vertices = [1, 2, 3]
edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]

# 인접 리스트 생성
mst = prim(vertices, edges)
print(mst)