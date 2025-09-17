def dfs(a, b, c):  # a : 수식에 사용할 숫자들, b : 연산자들, c : 연산자들의 길이는 필요 없을 지도?
    result = []  # 조합을 저장할 리스트

    if n == 1:
        return [[i] for i in b]

    for i in range(len(b)):
        elem = b[i]

        for rest in dfs(b[:i] + b[i+1:], n - 1):  # 순열
            result.append([elem] + rest)

    return result


test = int(input())
for t in range(1, test+1):
    n = int(input())  # 숫자의 개수
    o_list = list(map(int, input().split()))  # 연산자 갯수
    b_list = list(map(int, input().split()))  # 숫자들

    box = [[] for _ in range(len(b_list)*2)]  # 숫자들 사이에 빈 리스트 넣기(연산자 위해서)
    oper = [[] for _ in range(5)]
    for i in range(4):  # 0,1,2,3
        for j in range(o_list[i]):  
            print(i)
            oper[i+1].append(i+1)

    # print(box)
dfs(box, oper, len(oper))


# 5
# 2 1 0 1
# 3 5 3 7 9