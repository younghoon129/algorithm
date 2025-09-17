# 1. DFS 후위순회로 돌고 거꾸로 출력하면서 의존성 해결하며 문제 푸는 방법
# 2. Queue에 진입차수 0인 노드를 추가하고 꺼내면서 결과에 추가하며 Queue를 새로고침하는 방법


# 내가 짠 코드

# for t in range(1, 11):
# v, e = map(int, input().split())
# visited = [False] * (v+1)
# box = [[]*i for i in range(v+1)]
# b_list = list(map(int, input().split()))
# for i in range(0, len(b_list), 2):
#     box[b_list[i]].append(b_list[i+1])
# print(box)






# 위상정렬
    # 비순환 방향(DAG) 그래프에서만 가능 (사이클X, 방향 그래프)
    # 의존성/ 선후 관계 정하는 Algo
    # 유일한 해 보장 X
    # npm.pip(패키지 관리), 작업 스케쥴링에 사용

# 수업코드 1

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from collections import defaultdict

# def dfs(v):
#     visited[v] = True  # v번 인덱스 방문한 적 있는 지
#     for neighbor in graph[v]:  # graph[v] == v번이 방문할 인덱스들 순회
#         if not visited[neighbor]:  # 방문할 인덱스에 방문한 적 있는 지
#             dfs(neighbor)
#     result.append(v)
# T = 10
# for tc in range(1, T+1):
#     v_cnt, e_cnt = map(int, input().split())  # 9, 9 (정점, 간선의 개수)
#     edges = list(map(int, input().split()))  # 정점1 -> 정점2 에 대한 간선 리스트

#     # DAG 그래프 구성(방향그래프 구성이다)
#     # 인접리스트 형태(가장 많이 쓰임 외우자)
#     graph = defaultdict(list)
    
    
#     # 시작점과 끝정점을 서로 연결해준다
#     for i in range(e_cnt):
#         graph[edges[2*i]].append(edges[2*i+1])
#         # graph[edges[2*i+1]].append(edges[2*i]) -> 무방향이면 이것도 필요함
        
#     visited = [False] * (v_cnt + 1)
#     result = []

#     for v in range(1, v_cnt + 1):
#         if not visited[v]:
#             dfs(v)
#     print(f"#{tc}", *result[::-1])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# 수업코드 2

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

from collections import deque, defaultdict

T = 10
for tc in range(1, T+1):
    v_cnt, e_cnt = map(int, input().split())  # 9, 9 (정점, 간선의 개수)
    
    
    edges = list(map(int, input().split()))  # 정점1 -> 정점2 에 대한 간선 리스트

    # DAG 그래프 구성(방향그래프 구성이다)
    # 인접리스트 형태(가장 많이 쓰임 외우자)
    graph = defaultdict(list)
    

    # 시작점과 끝정점을 서로 연결해준다
    for i in range(e_cnt):
        graph[edges[2*i]].append(edges[2*i+1])
    # print(graph[1])

    in_degree = [0] * (v_cnt+1)

    # 
    for node in graph:  # node는 키 값 순회, node는 시작 정점임
        # print(node)        
        # 아 neighbor가 graph라는 큰 리스트의 node번에 있는 방문해야될 숫자들이네
        for neighbor in graph[node]:  # node(시작 정점)의 인접한 노드를 순회하면서, 진입 차수를 +1씩 해줌
            in_degree[neighbor] += 1
    

    queue = deque()
    for i in range(1, v_cnt+1):
        if in_degree[i] == 0:
            queue.append(i)
    # print(queue)

    result = []
    while queue:  # 진입차수 0인게 없어질 때까지
        node = queue.popleft()
        # print(node, 'while 안에 node')
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1  # in_degree == 진입차수
            if in_degree[neighbor] == 0:
                queue.append(neighbor)


    # 출력 결과가 노드 갯수 만큼 나와야 되는데 그렇지 않을 경우
    # 진입 차수 0이 없거나 싸이클이 있다는 의미
    if len(result) != v_cnt:  
        pass

    print(f"#{tc}", *result)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from collections import deque, defaultdict

# T = 10
# for tc in range(1, T+1):
#     v_cnt, e_cnt = map(int, input().split())  # 9, 9 (정점, 간선의 개수)
    
#     edges = list(map(int, input().split()))  # 정점1 -> 정점2 에 대한 간선 리스트

#     graph = defaultdict(list)

#     for i in range(e_cnt):
#         graph[edges[2*i]].append(edges[2*i+1])

#     in_degree = [0] * (v_cnt+1)

#     for node in graph:
#         for neighbor in graph[node]:
#             in_degree[neighbor] += 1
    

#     queue = deque()
#     for i in range(1, v_cnt+1):
#         if in_degree[i] == 0:
#             queue.append(i)

#     result = []
#     while queue:
#         node = queue.popleft()
#         result.append(node)
#         for neighbor in graph[node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#     if len(result) != v_cnt:  
#         pass

#     print(f"#{tc}", *result)