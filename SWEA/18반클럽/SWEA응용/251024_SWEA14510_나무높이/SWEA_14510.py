T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_h = max(arr)
    diffs = [max_h - v for v in arr]
    need1 = 0
    need2 = 0
    for diff in diffs:
        need1 += diff % 2
        need2 += diff // 2
    # print(need1, need2)

    day = 0
    while need1 > 0 or need2 > 0:
        day += 1
        if day % 2 == 1:
            if need1 > 0:
                need1 -= 1
            elif need2 > 1:
                need2 -= 1
                need1 += 1
        else:
            if need2 > 0:
                need2 -= 1
    print(f'#{t + 1}', day)