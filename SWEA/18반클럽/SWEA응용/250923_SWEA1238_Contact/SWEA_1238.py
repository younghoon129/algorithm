from collections import deque

tc = 10  # 10개로 바꿔야 됨
for t in range(1, tc+1):
    n, m = map(int, input().split())  # n = 갯수, m = 시작점
    box = list(map(int, input().split()))
    cnt = 0  # 방문 순서
    max_cnt = 0 
    p = 0  # 결과(마지막 연락 받은 사람)
    queue = deque()
    visited = [0]*(max(box)+1)  # 전화 받은 상태 방문하면 cnt+= 1해서 넣자
    p_list = [[] for _ in range(max(box)+1)]

    for i in range(len(box)//2):
        # x 에서 y를 부모
        x, y = box[i*2], box[(i*2)+1]
        p_list[x].append(y)
    queue.append(m)
    visited[m] = True  # m번 방문
    while queue:
        size = len(queue)  # 2 하나이니까
        result = []  # 만약 다음 이동할 거 있으면 초기화 후 새로 받음
        p = 0
        for k in range(size):  # queue에 있는 만큼
            a = queue.popleft()  # 하나씩 다 빼오기
            result.append(a)  # queue에 있는 거 다 넣기
            p = max(result)  # 결과 값인데 result중에 가장 큰거랑 p랑 비교해서 넣음
            for l in p_list[a]:  # p_list의 2번 안에 있는 거 다 꺼내와
                if not visited[l]:  # 그 번호들 간 적 없으면 아래 실행
                    queue.append(l)  # 간 적 없으면 큐에 넣기
                    visited[l] = True

    print(f"#{t} {p}")



# 24 2
# 100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2


# 100 17
# 39 22
# 100 8
# 100 7
# 7 100
# 2 7
# 2 15
# 15 4
# 6 2
# 11 6
# 4 10
# 4 2