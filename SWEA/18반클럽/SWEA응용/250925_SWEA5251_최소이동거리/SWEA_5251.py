from collections import defaultdict
import heapq, math

def dijkstra(graph, start):
    distances = {v : math.inf for v in graph}
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        c_distance, c_vertex = heapq.heappop(min_heap)
        # print(c_distance, c_vertex, '@@@@@@@@@')
        if distances[c_vertex] < c_distance: continue
        for adjacent, weight in graph[c_vertex].items():
            distance = c_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(min_heap, [distance, adjacent])
    return distances, graph

tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(m)]
    graph = defaultdict(dict)
    for i in range(n+1):
        graph[i]
    print(graph)
    for j in range(m):
        graph[box[j][0]].update({box[j][1] : box[j][2]})
    # print(graph)
    result = dijkstra(graph, 0)
    print(f"#{t} {result}")

