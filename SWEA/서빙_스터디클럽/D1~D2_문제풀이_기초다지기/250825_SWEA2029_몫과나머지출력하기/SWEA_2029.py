# 23:32 ~ 23:35
test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    print(f"#{t} {n//m} {n % m}")