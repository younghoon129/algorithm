# def dfs(arr, c):
#     if arr == chd1:
#         pass
#     elif arr == chd2:
#         pass
    


# test = int(input())

# for t in range(1, test+1):
#     v, e, chd1, chd2 = map(int, input().split())
#     b_list = list(map(int, input().split()))
#     box = [[] for _ in range(v+1)]
#     for i in range(0, len(b_list), 2):
#         box[b_list[i]].append(b_list[i+1])
    


#     dfs(box, 1)

# 내 코드


# 수업 코드

"""
LCA(최소 공통 조상)
- Git 두 브랜치의 공통 조상을 찾을 때
- 네트워크에서 "라우팅" 경로 최적화
- 디렉토리 공통 상위 디렉토리를 찾을 때도 써요

=>
1. 각 노드의 부모 노드, 깊이, 서브트리를 미리 구해놓는다. (DFS)
2. 우리가 구하고 싶은 노드들의 깊이를 맞춘다.
3. 서로 부모로 올라가면서 같은 값인지 비교하고, 같으면 걔는 공통조상
"""


# def dfs(node, depth):
#     # 해당 접근 노드의 깊이를 저장해준다.
#     depths[node] = depth

#     # 방문하지 않은 노드들을 DFS로 방문합니다.
#     # node의 자식노드들을 순회하는 코드
#     for child in tree[node]:
#         # 접근하는 자식 노드들의 입장에서는 "현재 노드"가 부모인거다.
#         parent[child] = node
#         # 자식 노드에 대해서 DFS를 실생했으니까 depth + 1 해서 보내준다.
#         dfs(child, depth + 1)

#     ########## 코드가 이 쪽에 도달했다는 의미는 더 이상 진행할 곳이 없다는 의미에요
#     subtree_size[node] = 1  # 서브트리 크기에 본인 노드를 포함시킨다.
#     # 자식 노드들의 서브트리 크기를 더해준다.
#     # 리프노드가 왔따면, 자식이 없기 때문에 서브트리 개수는 1개로 설정되고 끝난다.
#     for child in tree[node]:  
#         subtree_size[node] += subtree_size[child]


# # 정점 2개가 주어졌을 때, 최소 공통 조상을 찾는 함수
# def lca(a, b):
#     # 두 노드의 깊이가 다르다면, 더 깊은 노드가 얕은 노드와 같아질 때까지 끌어 올린다.
#     while depths[a] != depths[b]:
#         if depths[a] > depths[b]:  # a가 더 깊숙히 있다.
#             # a를 a의 부모로 바꾼다.
#             a = parent[a]
#         else:  # b가 더 깊숙히 있다.
#             b = parent[b]

#     # 여기에 도달했다는건, a와b의 높이가 맞춰졌다는 의미
#     # a와b가 같으면 공통 조상인거고, 다르면 둘다 부모로 한칸씩 올라간다.
#     while a != b:
#         a = parent[a]
#         b = parent[b]

#     # 여기에 도달했다는건, 같아졌다는 의미이다.
#     # 공통조상을 반환한다.
#     return a


# T = int(input())
# for tc in range(1, T + 1):
#     # 정점 수, 간선 수, 두 정점 a, b 입력
#     v_cnt, e_cnt, a_vertex, b_vertex = map(int, input().split())
#     edges = list(map(int, input().split()))

#     # 트리를 구성했다.
#     tree = [[] for _ in range(v_cnt + 1)]  
    
#     for i in range(e_cnt):
#         tree[edges[2 * i]].append(edges[2 * i + 1])

#     # 부모의 정점 번호를 인덱스로써 활용할거다. (번호는 1부터 시작하니까, 1칸 크게 초기화)
#     # 각 노드의 부모 노드를 저장(부모노드를 찾아서 올라가기 위해서)
#     parent = [0] * (v_cnt + 1)
#     # 각 노드의 깊이를 저장 (공통조상을 찾기 위한 두 노드의 깊이를 맞추기 위해서)
#     depths = [0] * (v_cnt + 1)
#     # 각 노드의 서브트리 크기를 저장할 변수
#     subtree_size = [0] * (v_cnt + 1)  

#     # DFS를 수행하면서, 트리를 탐색하면서 모든 노드의 부모/깊이/서브트리 크기를 구한다.
#     # 1번 노드를 시작점으로 잡고, 0번 깊이부터 시작한다.
#     dfs(1, 0)

#     common_res = lca(a_vertex, b_vertex)  

#     print(f"#{tc} {common_res} {subtree_size[common_res]}")

def dfs(node, depth):
    # 해당 접근 노드의 깊이를 저장해준다.
    depths[node] = depth

    # 방문하지 않은 노드들을 DFS로 방문
    # node의 자식노드들을 순회하는 코드
    for child in tree[node]:
        # 접근하는 자식노드들의 입장에서 현재 'node'가 부모
        parent[child] = node
        
        # 자식 노드에 대해서 DFS를 실행했으니 depth + 1 해서 보내줌
        dfs(child, depth + 1)
    subtree_size[node] = 1  # 서브트리 크기에 본인 노드를 포함
    # 자식 노드들의 서브트리 크기를 더함
    # 리프노드가 오면, 자식이 없으니 서브트리 개수는 1개로 설정됨
    for child in tree[node]:  # 각 서브부모들의 자식들 검사
        subtree_size[node] += subtree_size[child]



# 정점 2개가 주어졌을 때, 최소 공통 조상을 찾는 함수
def lca(a,b):
    # 두 노드의 깊이가 다르다면, 더 깊은 노드가 얕은 노드와 같아질 때까지 끌어 올림
    while depths[a] != depths[b]:
        if depths[a] > depths[b]:  # a가 더 깊숙히 있다.
            # a를 a의 부모로 변경
            a = parent[a]
        else:  # b가 더 깊숙히 있다.
            b = parent[b]

    # 여기 도달하면, a와 b 높이 맞춰졋다는 의미
    # a와b가 같으면 공통 조상, 다르면 부모로 한칸씩 이동
    while a!=b:
        a = parent[a]
        b = parent[b]

    # 여긴 같아졌다는 의미
    # 공통조상 a ㄱㄱ
    return a




T = int(input())
for tc in range(1, T+1):
    v_cnt, e_cnt, a_vertex, b_vertex = map(int, input().split())  
    edges = list(map(int, input().split()))

    tree = [[] for _ in range(v_cnt + 1)]

    for i in range(e_cnt):
        tree[edges[2 * i]].append(edges[2*i+1])

    # 부모의 정점 노드를 인덱스로써 활용
    # 각 노드의 부모 노드를 저장(부모노드를 찾아서 올라가기 위해)
    parent = [0] * (v_cnt + 1)
    
    # 각 노드의 깊이를 저장(공통조상을 찾기 위한 두 노드의 깊이를 맞추기 위해)
    depths = [0] * (v_cnt + 1)

    # 각 노드의 서브트리 크기를 저장할 변수
    subtree_size = [0] * (v_cnt + 1)

    # DFS를 수행하면서, 트리를 탐색하면서 모든 노드의 부모/깊이/서브트리 크기를 구한다.
    # 1번 노드를 시작점으로 잡고, 0번 깊이부터 시작
    dfs(1, 0)

    common_res = lca(a_vertex, b_vertex)