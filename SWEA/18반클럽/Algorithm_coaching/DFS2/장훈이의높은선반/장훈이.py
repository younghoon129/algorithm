def dfs(arr, n):
    result = 100  # 조합을 저장할 리스트

    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]

        for rest in dfs(arr[i + 1:], n - 1):  # 조합
            if bs - [elem] + rest >= b:
                result = min(result, bs - [elem] + rest)


    return result


test = int(input())

for t in range(1, test+1):
    n, b = map(int, input().split())
    box = list(map(int, input().split()))
    bs = sum(box)

for i in range(n):
    print(dfs(box, i))
