# 22: 38 ~ 22 : 41
test = int(input())

for t in range(1, test+1):
    n = list(map(int, input().split()))
    result = sum(n)/len(n)
    print(f"#{t} {result:.0f}")
