# 13:50

def bino(n, k):
    B = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i -1][j]
    return B[n][k]

tc = int(input())
for t in range(1, tc+1):
    n, a, b = map(int, input().split())
    result = bino(n, a)
    print(f"#{t} {result}")


# 3
# 2 1 1
# 3 2 1
# 5 3 2