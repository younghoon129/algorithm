for q in range(3):
    n = int(input())
    box1 = list(map(int, input().split()))
    print(box1)
    box2 = list(map(int, input().split()))
    for i in range(n):
        if box1[i] != box2[i]:
            for j in range(i, n):
                box1[j] ^= 1
    print(box1)


# 1 1 1 1 1 0 0 0 1 1
# 1 1 0 1 1 0 1 1 0 0