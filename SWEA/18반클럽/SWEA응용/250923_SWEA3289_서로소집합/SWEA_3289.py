def find_set(x):
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
    result = ''
    p_list = list(range(n+1))
    rank = [0]*(n+1)
    for i in range(m):
        h, x, y = map(int, input().split())
        if h == 0:
            union_set(x, y)
        else:
            if find_set(x) == find_set(y):
                result+='1'
            else:
                result+='0'
    

    print(f"#{t} {result}")