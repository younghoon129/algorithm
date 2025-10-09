tc = int(input())

for t in range(1, tc+1):
    n, l = map(int, input().split())
    items = []
    table = [[0] * (l+1) for _ in range(n+1)]
    # for i in range(1, n+1):
    #     score, k = map(int, input().split())

    #     for j in range(1, l+1):
    #         if k <= j:
    #             table[i][j] = max
print(table)