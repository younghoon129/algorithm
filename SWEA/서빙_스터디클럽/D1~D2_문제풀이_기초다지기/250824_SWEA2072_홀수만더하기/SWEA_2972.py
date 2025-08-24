# 22:34 ~ 22:36
test = int(input())

for t in range(1, test+1):
    n = list(map(int, input().split()))
    m = 0
    for i in n:
        if i % 2 != 0:
            m += i
    print(f"#{t} {m}")