def hambuger(idx, s_num, k_num):  # sk : 맛, 칼
    global s_sum_num
    if k_num > l:
        return
    s_sum_num = max(s_sum_num, s_num)
    if idx == n:
        return
    for i in range(idx, n):
        hambuger(i+1, s_num+sk[i][0], k_num+sk[i][1])
        # hambuger(i+1, s_num, k_num)
        

tc = int(input())
for t in range(1, tc+1):
    n, l = map(int, input().split())
    s_sum_num = 0
    k_num = 0
    s_num = 0
    sk = []
    for i in range(n):
        sk.append(tuple(map(int, input().split())))

    hambuger(0, s_num, k_num)

    print(f"#{t} {s_sum_num}")

# 1
# 5 1000
# 100 200
# 300 500
# 250 300
# 500 1000
# 400 400