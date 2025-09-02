# 13:55 : 14:19

test = int(input())
for t in range(1, test+1):
    n = int(input())
    se = [list(map(int, input().split())) for _ in range(n)]
    se.sort(key=lambda x : x[1])
    x = se[0][1]
    cnt = 1
    while True:
        i = 0
        while True:
            if x <= se[i][0]:
                x= se[i][1]
                cnt += 1
            i += 1
            if i == n:
                break
        if i == n:
            break
    print(f"#{t} {cnt}")