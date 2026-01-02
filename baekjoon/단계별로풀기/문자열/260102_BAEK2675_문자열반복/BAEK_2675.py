n = int(input())
for i in range(n):
    a = input().split()
    result = ''
    for j in range(len(a[1])):
        for k in range(int(a[0])):
            result+=a[1][j]
    print(result)
