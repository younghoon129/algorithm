# 30분
def find_set(x):
    if x not in p_list[x]:
        p_list[x].append(find_set(p_list[x]))
    return p_list[x]


def union_set(x, y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        p_list[px].append(py)


def dfs(p_list, m):
    global cnt, max_cnt, p
    if cnt > max_cnt:
        max_cnt = cnt
        p = 
    pass



tc = 1  # 10개로 바꿔야 됨
for t in range(1, tc+1):
    n, m = map(int, input().split())  # n = 갯수, m = 시작점
    box = list(map(int, input().split()))
    cnt = 0  # 방문 순서
    max_cnt = 0 
    p = 0  # 결과(마지막 연락 받은 사람)
    visited = [[0] for _ in range(max(box)+1)]  # 전화 받은 상태 방문하면 cnt+= 1해서 넣자
    p_list = [[0] for _ in range(max(box)+1)]
    for i in range(len(box)//2):
        # x 에서 y를 부모
        x, y = box[i*2], box[(i*2)+1]
        # union_set(x, y)
        p_list[x].append(y)
    for j in range(1, len(p_list)):
        for k in range(len(p_list[j])):
            if p_list[j][k]:
                print(p_list[j][k])
        # print(p_list[j])
    # print(p_list)









# 24 2
# 100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2