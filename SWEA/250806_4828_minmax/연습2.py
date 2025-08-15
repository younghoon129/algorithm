test = int(input())

for t in range(1, test+1):
    x = int(input())
    n = list(map(int, input().split()))
    m = max(n)
    mi = min(n)
    print(f"#{t} {m-mi}")
