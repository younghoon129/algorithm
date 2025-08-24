# 22: 46 ~ 22 : 46
test = int(input())

for t in range(1, test+1):
    n = list(map(int, input().split()))
    print(f"#{t} {max(n)}")
