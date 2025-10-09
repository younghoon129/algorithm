from collections import deque

def find_set(x):
    if x != box[x]:
        box[x] = find_set(box[x])
    return box[x]

def union_set(x, y):
    lx = find_set(x)
    ry = find_set(y)
    if lx != ry:
        if rank[lx] > rank[ry]:
            box[ry] = box[lx]
        elif rank[lx] < rank[ry]:
            box[lx] = box[ry]
        else:
            box[lx] = box[ry]
            rank[ry] += 1



tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    box = list(range(n+1))
    rank = list(range(n+1))
    max_cnt = 0
    for i in range(m):
        l, r = map(int, input().split())
        union_set(l, r)
    for j in range(len(box)):
        find_set(j)
    result = set(box)
    for k in result:
        max_cnt = max(max_cnt, box.count(k))
    print(f"#{t} {max_cnt}")