# 11:11 ~ 11:34
test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    wi.sort(reverse=True)  # 화물
    ti.sort(reverse=True)  # 트럭
    cnt = 0
    a= min(n,m)
    b = False
    for i in range(len(ti)):

        for j in range(len(wi)):
            if ti[i] >= wi[j]:
                cnt += wi[j]
                wi.pop(j)
                break
            elif ti[i] < min(wi):
                b = True
                break
        if b:
            break
    print(f"#{t} {cnt}")