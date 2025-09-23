def find_set(x):
    if x == 0:
        return
    if x != p_list[x]:
        p_list[x] = find_set(p_list[x])

    return p_list[x]

def union_set(x, y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        if rank[px] > rank[py]:
            p_list[py] = px
        elif rank[px] < rank[py]:
            p_list[px] = py
        else:
            p_list[py] = px
            rank[px] += 1

tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    p_list = list(range(n+1))
    rank = [0]*(n+1)  # 0~6
    box = [list(map(int, input().split())) for _ in range(m)]
    muri = []
    for i in range(m):
        for j in range(len(box[i])):
            muri.append(box[i][j])

    for j in range(m):
        x = muri[j*2]
        y = muri[j*2+1]
        union_set(x, y)

    for i in range(1, n+1):
        p_list[i] = find_set(i)

    print(f"#{t} {len(set(p_list))-1}")