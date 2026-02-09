n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        result = matrix_a[i][j] + matrix_b[i][j]
        print(result, end=' ')
    print()