def find_set(x):
    if x != pl[x]:
        pl[x] = find_set(pl[x])
    return pl[x]

def union_set(x, y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        if rank[px] > rank[py]:
            pl[py] = px
        elif rank[px] < rank[py]:
            pl[px] = py
        else:
            pl[py] = px
            rank[px] += 1

tc = int(input())

for t in range(1, tc+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(m)]
    friend = [[] for _ in range(n+1)]
    pl = list(range(n+1))
    rank = [0]*(n+1)
    for i in range(m):
        friend[box[i][0]].append(box[i][1])
    for j in range(m):
        x, y = box[j][0], box[j][1]
        union_set(x, y)
    
    for k in range(1, n+1):
        pl[k] = find_set(pl[k])

    print(f"#{t} {len(set(pl))-1}")

      
    
# 2
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3
