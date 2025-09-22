success = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def alpha(result, idx):
    global cnt
    if len(success) == len(result):
        cnt += 1
        return
    if idx == n:
        return

    for i in range(idx, n):
        for j in range(len(box[i])):
            result.add(box[i][j])
        alpha(result, i+1)

        for j in range(len(box[i])):
            result.discard(box[i][j])
        alpha(result, i+1)

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = [list(map(str, input())) for _ in range(n)]
    result = set([])
    cnt = 0

    alpha(result, 0)
    print(f"#{t} {cnt}")