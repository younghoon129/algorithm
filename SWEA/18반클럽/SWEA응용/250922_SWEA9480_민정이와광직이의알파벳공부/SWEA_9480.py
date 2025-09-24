success = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def alpha(result, idx):
    global cnt
    if len(success) == len(result):
        cnt += 1
        return
    if idx == n:
        return

    for i in range(idx, n):
        result2 = set(box[i])
        print(result2)
        alpha(result | result2, i+1)
        alpha(result, i+1)

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = [list(map(str, input())) for _ in range(n)]
    result = set()
    cnt = 0

    alpha(result, 0)
    print(f"#{t} {cnt}")





# def alpha(result, idx):
#     global cnt
#     if len(result) == 26:
#         cnt += 1
#         return
#     if idx == n:
#         return

#     for i in range(idx, n):
#         result2 = set(box[i])
#         alpha(result | result2, i+1)  # 포함
#         alpha(result, i+1)           # 미포함

# tc = int(input())
# for t in range(1, tc+1):
#     n = int(input())
#     box = [list(input().strip()) for _ in range(n)]
#     cnt = 0

#     alpha(set(), 0)
#     print(f"#{t} {cnt}")
